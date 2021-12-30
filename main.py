from morse import morse
from flask import Flask, render_template, request
from datetime import datetime
from playsound import playsound
from pydub import AudioSegment
import sys

# sys.path.append("/Users/adriancaso/Downloads/ffmpeg")
# sys.path.append("/Users/adriancaso/Downloads/ffprobe")
app = Flask(__name__)
year = datetime.now().year


@app.route('/', methods=['GET', 'POST'])
def home():
    translation = ""
    audio_list = None
    if request.method == "POST":
        text = request.form.get('translate-text')
        translation = translate(text)
        audio_list = create_combined_mp3(make_mp3(translation))
    return render_template('index.html', text=translation, year=year, audio=audio_list)


def translate(txt_input):
    output = ""
    for letter in txt_input:
        if letter.upper() not in morse:
            pass
        else:
            output += morse[letter.upper()] + "  "
    return output


def make_mp3(morse_string):
    sound_file = ["pause.mp3"]
    for beep in morse_string:
        if beep == ".":
            sound_file.append("dit.mp3")
        elif beep == "-":
            sound_file.append("dah.mp3")
        elif beep == " ":
            sound_file.append("pause.mp3")
        else:
            pass
    print(sound_file)
    return sound_file


def play_mp3(file_list):
    for file in file_list:
        playsound(file)


if __name__ == "__!main__":
    app.run(debug=True)


# def combine_audio(morse_string):
#     sound1 = AudioSegment.from_file("/Users/adriancaso/PycharmProjects/string-to-morsecode/pause.mp3")
#     combined = None
#     combined += sound1
#     for index, file in enumerate(morse_string):
#         combined += AudioSegment.from_file(f"{file}")
#     combined.export("/Users/adriancaso/PycharmProjects/string-to-morsecode/output.mp3")
#
#
# def create_combined_mp3(file_list):
#     combined = AudioSegment.append(file_list, seg="true")
#     combined.export("/Users/adriancaso/PycharmProjects/string-to-morsecode/output.mp3")


def create_combined_mp3(data):
    variable_names = {
        "a": None,
        "b": None,
        "c": None,
        "d": None,
        "e": None,
        "f": None,
        "g": None,
        "h": None,
        "i": None,
        "j": None,
        "k": None,
        "l": None,
        "m": None,
        "n": None,
        "o": None,
        "p": None,
        "q": None,
        "r": None,
        "s": None,
        "t": None,
        "u": None,
        "v": None,
    }

    identifiers = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                   'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v']

    for data_index, entry in enumerate(variable_names):
        try:
            variable_names[entry] = AudioSegment.from_file(data[data_index])
        except IndexError:
            pass

    combined = variable_names['a']

    for index, name in enumerate(variable_names):
        try:
            combined += variable_names[identifiers[index]]
        except IndexError and TypeError:
            pass

    return combined.export("/Users/adriancaso/PycharmProjects/string-to-morsecode/output1.mp3")

# data = ["dit.mp3", "dah.mp3", "dah.mp3", "dit.mp3", "pause.mp3", "dit.mp3", "dah.mp3",
# "dah.mp3", "dit.mp3", "pause.mp3"]
# variable_names = {
#         "a": None,
#         "b": None,
#         "c": None,
#         "d": None,
#         "e": None,
#         "f": None,
#         "g": None,
#         "h": None,
#         "i": None,
#         "j": None,
#         "k": None,
#         "l": None,
#         "m": None,
#         "n": None,
#         "o": None,
#         "p": None,
#         "q": None,
#         "r": None,
#         "s": None,
#         "t": None,
#         "u": None,
#         "v": None,
#     }
#
# for index, entry in enumerate(variable_names):
#     try:
#         variable_names[entry] = AudioSegment.from_file(data[index])
#     except IndexError:
#         pass
#
# reminder of how combined audiosegment needs to be created
# all at once
# combined = variable_names['a'] + variable_names['b'] + variable_names['c'] + variable_names['d']
# + variable_names['e'] + variable_names['f'] + variable_names['g'] + variable_names['h'] + variable_names['i']
#
# or with beginning value preset then +=
# combined = variable_names['a']
# combined += variable_names['b']
# combined += variable_names['c']
#
#
# combined.export("/Users/adriancaso/PycharmProjects/string-to-morsecode/output.mp3")
# playsound('output.mp3')
