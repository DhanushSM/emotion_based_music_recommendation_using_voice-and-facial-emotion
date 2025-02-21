from flask import Flask, jsonify, render_template, request, Blueprint
from flask_cors import CORS
import speech_recognition as sr
import time
import csv
from transformers import pipeline

blueprint = Blueprint('voice', __name__)
CORS(blueprint)

# Load the emotion detection model
emotion_pipeline = pipeline("text-classification", model="bhadresh-savani/distilbert-base-uncased-emotion")

# Load the CSV file with recommendations
recommendations = {}
with open('emotion_videos.csv', mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        emotion_key = row['Emotion'].lower()
        if emotion_key not in recommendations:
            recommendations[emotion_key] = []
        recommendations[emotion_key].append({
            "title": row['Title'],
            "link": row['Link'],
            "category": row['Category']
        })

def analyze_emotion(text):
    """Analyze text to detect emotion and map to CSV labels."""
    results = emotion_pipeline(text)
    emotion = max(results, key=lambda x: x['score'])
    emotion_label = emotion['label'].lower()

    # Map model labels to CSV labels
    emotion_mapping = {
        "anger": "angry",
        "sadness": "sad",
        "joy": "happy",
        "fear": "fear",
        "disgust": "disgust",
        "surprise": "surprise",
        "neutral": "neutral"
    }
    return emotion_mapping.get(emotion_label, emotion_label)

@blueprint.route('/')
def voice_home():
    return render_template('voice.html')

@blueprint.route('/start-detection', methods=['GET'])
def start_detection():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        audio_data = []

        try:
            start_time = time.time()
            while time.time() - start_time < 10:
                try:
                    audio_chunk = recognizer.listen(source, timeout=10)
                    audio_data.append(audio_chunk)
                except sr.WaitTimeoutError:
                    return jsonify({"success": False, "message": "Listening timed out while waiting for phrase to start."})

            # Combine recorded audio
            combined_audio = sr.AudioData(b''.join([chunk.get_raw_data() for chunk in audio_data]), audio_data[0].sample_rate, audio_data[0].sample_width)

            # Convert speech to text
            text = recognizer.recognize_google(combined_audio)
            emotion = analyze_emotion(text)
            recommendations_list = recommendations.get(emotion, [])

            if recommendations_list:
                return jsonify({"success": True, "emotion": emotion, "recommendations": recommendations_list})
            else:
                return jsonify({"success": False, "message": f"No recommendations found for {emotion} emotion."})

        except sr.UnknownValueError:
            return jsonify({"success": False, "message": "Could not understand audio."})
        except sr.RequestError as e:
            return jsonify({"success": False, "message": f"Speech recognition request failed: {e}"})