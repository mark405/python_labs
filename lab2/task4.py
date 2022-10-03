import re


class TextAnalyser(object):
    def __init__(self, text):
        self.__text = text

    def get_number_of_symbols(self):
        return len(self.__text)

    def get_number_of_words(self):
        list_of_words = self.__text.split()
        return len(list_of_words)

    def get_number_of_sentences(self):
        list_of_sentences = re.split("! | ? | .", self.__text)
        return len(list_of_sentences) - 1


text_analyser = TextAnalyser("hello world?\nhello world.")

print(text_analyser.get_number_of_symbols())
print(text_analyser.get_number_of_words())
print(text_analyser.get_number_of_sentences())
