"""
    This project will verify if a string is a palindrome or not
"""
class sentence:
    def __init__(self, sentence = " "):
        self.__sentence = sentence.upper()

    def verifier(self):
        aux_sentence = self.__sentence.replace(" ", "")
        reverse_word = aux_sentence[::-1]
        if aux_sentence == reverse_word:
            return True
        else:
            return False
