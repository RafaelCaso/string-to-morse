from pydub import AudioSegment


def make_file_list(morse_string):
    sound_file = ["pause.mp3"]
    for beep in morse_string:
        if beep == ".":
            sound_file.append("dit.mp3")
        elif beep == "-":
            sound_file.append("dah.mp3")
        elif beep == " ":
            sound_file.append("pause.mp3")

    return sound_file


def create_combined_mp3(data):
    print(data)
    variable_dict = {}
    for i, file in enumerate(data):
        variable_dict[f'{i}'] = file
    print(variable_dict)

    variable_identifiers = [i for i in variable_dict]
    for data_index, entry in enumerate(variable_dict):
        try:
            variable_dict[entry] = AudioSegment.from_file(data[data_index])
        except IndexError:
            pass

    combined = variable_dict['0']
    for index, name in enumerate(variable_dict):
        try:
            combined += variable_dict[variable_identifiers[index]]
        except IndexError and TypeError:
            pass

    return combined.export("/Users/adriancaso/PycharmProjects/string-to-morsecode/static/output1.mp3")
