from flask import Flask, render_template, request, jsonify, Blueprint
import cv2
import base64
import numpy as np
from deepface import DeepFace
import csv

blueprint = Blueprint('video', __name__)

# Load face cascade classifier
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

def detect_emotion(frame):
    # Convert frame to grayscale
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Convert grayscale frame to RGB format
    rgb_frame = cv2.cvtColor(gray_frame, cv2.COLOR_GRAY2RGB)

    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    if len(faces) == 0:
        return None

    for (x, y, w, h) in faces:
        # Extract the face ROI (Region of Interest)
        face_roi = rgb_frame[y:y + h, x:x + w]

        # Perform emotion analysis on the face ROI
        result = DeepFace.analyze(face_roi, actions=['emotion'], enforce_detection=False)

        # Determine the dominant emotion
        emotion = result[0]['dominant_emotion']
        return emotion

def get_recommendations(emotion):
    recommendations = []
    categories = set()
    with open('emotion_videos.csv', mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            if row['Emotion'].lower() == emotion.lower():
                recommendations.append({'title': row['Title'], 'link': row['Link'], 'category': row['Category']})
                categories.add(row['Category'])
    return recommendations, list(categories)

@blueprint.route('/')
def video_home():
    return render_template('video_d.html')

@blueprint.route('/detect_emotion', methods=['POST'])
def detect_emotion_route():
    data = request.json['image']
    nparr = np.fromstring(base64.b64decode(data), np.uint8)
    frame = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    emotion = detect_emotion(frame)
    if emotion:
        recommendations, categories = get_recommendations(emotion)
        return jsonify({'emotion': emotion, 'recommendations': recommendations, 'categories': categories})
    else:
        return jsonify({'emotion': 'No face detected', 'recommendations': [], 'categories': []})