from morse import translate
from flask import Flask, render_template, request
from datetime import datetime
import audio
from flask_sqlalchemy import SQLAlchemy
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'thequickbrownfox'
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///morsecode.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
socketio = SocketIO(app)
db = SQLAlchemy(app)
year = datetime.now().year


class Message(db.Model):
    __tablename__ = "messages"
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String(250))
    morse_code = db.Column(db.String(250))


db.create_all()


@socketio.on('message')
def handle_message(data):
    print("received message " + data)


@app.route('/', methods=['GET', 'POST'])
def home():
    translation = ""
    audio_file = None
    if request.method == "POST":
        text = request.form.get('translate-text')
        translation = translate(text)
        audio_file = audio.create_combined_mp3(audio.make_file_list(translation))
        new_message = Message(
            message=text,
            morse_code=translation
        )
        db.session.add(new_message)
        db.session.commit()
    return render_template('index.html', text=translation, year=year, audio=audio_file)


@app.route('/register')
def register():
    return render_template('register.html', year=year)


@app.route('/login')
def login():
    return render_template('login.html', year=year)


if __name__ == "__main__":
    socketio.run(app, port=8080)
