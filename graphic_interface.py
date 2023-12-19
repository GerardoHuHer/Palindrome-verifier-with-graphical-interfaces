import tkinter as tk  
from main import Sentence

class Interface(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Palindrome Verifier")

        self.sentence_obj = Sentence()
        self.crear_interfaz()

    def crear_interfaz(self):
        entry_label = tk.Label(self, text = "Enter a word:")
        entry_label.pack(pady = 10)

        self.word_entry = tk.Entry(self, width = 30)
        self.word_entry.pack(pady = 10)

        verify_button = tk.Button(self, text = "Verify", command=self.verificar_palindromo)
        verify_button.pack(pady = 10)

        self.result_label = tk.Label(self, text = "")
        self.result_label.pack(pady = 10)

        quit = tk.Button(self, text = "Quit", command = self.quit_app)
        quit.pack(pady = 10)

    def verificar_palindromo(self):
        palabra = self.word_entry.get()

        self.sentence_obj = Sentence(palabra)

        its_palindrome = self.sentence_obj.verifier()

        resultado = "It's a Palindrome." if its_palindrome else "It is not a Palindrome."
        self.result_label.config(text = resultado)

    def quit_app(self):
        self.destroy()

if __name__ == "__main__":
    app = Interface()
    app.mainloop()
