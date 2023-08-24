import tkinter as tk

class MorseTranslatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Morse Code Translator")
        
        self.label = tk.Label(root, text="Enter text or Morse code:")
        self.label.pack(pady=10)
        
        self.input_text = tk.Entry(root)
        self.input_text.pack(padx=10, pady=5, fill=tk.X)
        
        self.translate_button = tk.Button(root, text="Translate", command=self.translate_text)
        self.translate_button.pack(pady=5)
        
        self.result_label = tk.Label(root, text="")
        self.result_label.pack(pady=10)
        
        self.clear_button = tk.Button(root, text="Clear", command=self.clear_text)
        self.clear_button.pack(pady=5)
        
    def translate_text(self):
        input_value = self.input_text.get().strip()
        
        if input_value.startswith('-') or input_value.startswith('.'):
            translated_text = self.morse_to_text(input_value)
        else:
            translated_text = self.text_to_morse(input_value)
        
        self.result_label.config(text=translated_text)
        
    def text_to_morse(self, text):
        morse_code_dict = {
            'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
            'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
            'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
            'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
            'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
            'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
            '3': '...--', '4': '....-', '5': '.....', '6': '-....',
            '7': '--...', '8': '---..', '9': '----.',
        }
        
        morse_code = []
        for char in text.upper():
            if char == ' ':
                morse_code.append(' ')
            else:
                morse_code.append(morse_code_dict.get(char, char))
        return ' '.join(morse_code)
        
    def morse_to_text(self, morse):
        morse_code_dict = {value: key for key, value in self.get_morse_code_dict().items()}
        text = []
        morse_parts = morse.split(' ')
        for part in morse_parts:
            if part == '':
                text.append(' ')
            else:
                text.append(morse_code_dict.get(part, part))
        return ''.join(text)
    
    def get_morse_code_dict(self):
        morse_code_dict = {
            'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
            'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
            'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
            'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
            'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
            'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
            '3': '...--', '4': '....-', '5': '.....', '6': '-....',
            '7': '--...', '8': '---..', '9': '----.',
        }
        return morse_code_dict
    
    def clear_text(self):
        self.input_text.delete(0, tk.END)
        self.result_label.config(text="")

def main():
    root = tk.Tk()
    app = MorseTranslatorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
