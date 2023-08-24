
morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.',
    '(': '-.--.', ')': '-.--.-', '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-',
    '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.', '$': '...-..-', '@': '.--.-.'
}


def text_to_morse(text):
    morse_code = []
    for char in text.upper():
        if char == ' ':
            morse_code.append(' ')
        else:
            morse_code.append(morse_code_dict.get(char, char))
    return ' '.join(morse_code)


def morse_to_text(morse):
    text = []
    morse_parts = morse.split(' ')
    for part in morse_parts:
        if part == '':
            text.append(' ')
        else:
            text.append(next((char for char, code in morse_code_dict.items() if code == part), part))
    return ''.join(text)


user_input = input("Ingresa un mensaje en texto o código Morse: ")
if '-' in user_input or '.' in user_input:
    translated_text = morse_to_text(user_input)
    print("Texto traducido:", translated_text)
else:
    morse_code = text_to_morse(user_input)
    print("Código Morse:", morse_code)
