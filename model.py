class Model:
    def __init__(self, text_file):
        self.text_file = text_file

    @property
    def text_file(self):
        return self.__text_file

    @text_file.setter
    def text_file(self, value):
        self.__text_file = value
