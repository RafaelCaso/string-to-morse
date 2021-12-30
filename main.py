from morse import morse
from flask import Flask, render_template, request
from datetime import datetime
import audio

app = Flask(__name__)
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


def translate(txt_input):
    output = ""
    for letter in txt_input:
        if letter.upper() not in morse:
            pass
        else:
            output += morse[letter.upper()] + " "
    return output


if __name__ == "__main__":
    app.run(debug=True)
