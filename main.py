from morse_dict import morse_dict


def string_to_morse(user_input):

    morse_string = [morse_dict[char] for char in user_input]

    morse_code = ""
    for char in morse_string:
        morse_code += " " + char

    return morse_code


while True:
    print("Type 'exit' to stop")
    text_to_convert = input("Type the text that you want to convert to Morse code: \n").upper()

    if text_to_convert == "EXIT":
        break

    try:
        converted_text = string_to_morse(text_to_convert)
        print(converted_text)

    except KeyError:
        print("You typed a character that could not be translated. Try again...")



