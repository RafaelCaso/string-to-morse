from morse import translate
from flask import Flask, render_template, request
from datetime import datetime
import audio
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///morsecode.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
year = datetime.now().year


@app.route('/', methods=['GET', 'POST'])
def home():
    translation = ""
    audio_list = None
    if request.method == "POST":
        text = request.form.get('translate-text')
        translation = translate(text)
        audio_list = audio.create_combined_mp3(audio.make_file_list(translation))
    return render_template('index.html', text=translation, year=year, audio=audio_list)


@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/login')
def login():
    return render_template('login.html')


if __name__ == "__main__":
    app.run(debug=True)
