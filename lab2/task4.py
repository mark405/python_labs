import re
import os.path


class TextAnalyser(object):
    def __init__(self, file_name):
        if os.path.exists(file_name):
            self.__file_name = file_name
        else:
            raise NameError

    def read_file(self):
        text = ""
        with open(self.__file_name, "r") as f:
            for line in f:
                text += line

        return text

    def get_number_of_symbols(self):
        res = len(self.read_file())
        return res

    def get_number_of_words(self):
        res = len(re.findall(r'\w+', self.read_file()))
        return res

    def get_number_of_sentences(self):
        res = len(re.split(r'[.?!]', self.read_file())) - 1
        return res

    def get_number_of_lines(self):
        res = len(re.split(r'\n', self.read_file())) - 1
        return res


try:
    text_analyser = TextAnalyser("/Users/markzavgorodniy/Desktop/text.txt")

    print(text_analyser.get_number_of_symbols())
    print(text_analyser.get_number_of_words())
    print(text_analyser.get_number_of_sentences())
    print(text_analyser.get_number_of_lines())
except NameError:
    print("NameError")
