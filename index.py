from flask import Flask, render_template
import voice
import video

app = Flask(__name__)

# Register blueprints
app.register_blueprint(voice.blueprint, url_prefix='/voice')
app.register_blueprint(video.blueprint, url_prefix='/video')

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)