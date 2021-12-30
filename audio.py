from playsound import playsound
from pydub import AudioSegment


def make_mp3(morse_string):
    sound_file = ["pause.mp3"]
    for beep in morse_string:
        if beep == ".":
            sound_file.append("dit.mp3")
        elif beep == "-":
            sound_file.append("dah.mp3")
        elif beep == "":
            sound_file.append("pause.mp3")
        else:
            pass
    return sound_file


def play_mp3(file_list):
    for file in file_list:
        playsound(file)





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
    print(data)
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
        "w": None,
        "x": None,
        "y": None,
        "z": None,
        "aa": None,
        "bb": None,
        "cc": None,
        "dd": None,
        "ee": None,
        "ff": None,
        "gg": None,
        "hh": None,
        "ii": None,
        "jj": None,
        "kk": None,
        "ll": None,
        "mm": None,
        "nn": None,
        "oo": None,
        "pp": None,
        "qq": None,
        "rr": None,
    }

    identifiers = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k','l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'aa', 'bb', 'cc', 'dd', 'ee', 'ff', 'gg', 'hh', 'ii', 'jj', 'kk', 'll', 'mm', 'nn', 'oo', 'pp', 'qq', 'rr']

    for data_index, entry in enumerate(variable_names):
        try:
            variable_names[entry] = AudioSegment.from_file(data[data_index])
        except IndexError:
            pass
    print(variable_names)
    combined = variable_names['a']

    for index, name in enumerate(variable_names):
        try:
            combined += variable_names[identifiers[index]]
        except IndexError and TypeError:
            pass

    return combined.export("/Users/adriancaso/PycharmProjects/string-to-morsecode/static/output1.mp3")

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