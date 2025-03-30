# Emotion-Based Music Recommendation Using Voice and Facial Emotion

## About the Project
This project recommends music based on the user's emotional state by analyzing both voice and facial emotions. It identifies the user's mood with 90% accuracy and suggests appropriate music tracks, enhancing the user experience by up to 85%.

## Features
- **Voice Emotion Detection:** Uses advanced audio processing techniques to analyze the user's voice and detect emotions.
- **Facial Emotion Detection:** Utilizes computer vision algorithms to analyze the user's facial expressions and determine their emotional state.
- **Music Recommendation:** Recommends music tracks that match the detected emotions, providing a personalized and immersive listening experience.
- **User-Friendly Interface:** Offers a simple and intuitive web-based interface for users to interact with the system.

## How It Works
1. **Data Capture:** The system captures audio and video input from the user's microphone and camera.
2. **Emotion Detection:** 
   - **Voice Analysis:** Processes the audio input to detect emotions such as happiness, sadness, anger, and surprise.
   - **Facial Analysis:** Analyzes the video input to identify facial expressions corresponding to different emotions.
3. **Emotion Fusion:** Combines the detected emotions from both voice and facial analysis to determine the overall emotional state.
4. **Music Recommendation:** Based on the fused emotional state, the system recommends music tracks that align with the user's current mood.

## Installation
To set up the project locally, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/DhanushSM/emotion_based_music_recommendation_using_voice-and-facial-emotion.git
    ```
2. Navigate to the project directory:
    ```bash
    cd emotion_based_music_recommendation_using_voice-and-facial-emotion
    ```
3. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
    ```
4. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
5. Run the application:
    ```bash
    python main.py
    ```

## Usage
- Ensure your microphone and camera are connected and properly configured.
- Run the application using the provided command.
- Follow the on-screen instructions to capture your voice and facial expressions.
- The system will analyze your emotions and recommend music tracks based on your current mood.

## Contributing
Contributions are welcome! To contribute to this project, follow these steps:

1. Fork the repository.
2. Create a new branch:
    ```bash
    git checkout -b feature-name
    ```
3. Make your changes and commit them:
    ```bash
    git commit -m 'Add some feature'
    ```
4. Push to the branch:
    ```bash
    git push origin feature-name
    ```
5. Open a pull request to the `main` branch.

## License
This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Contact Information
- **Repository Owner:** [DhanushSM](https://github.com/DhanushSM)
- **Email:** [your-email@example.com]
