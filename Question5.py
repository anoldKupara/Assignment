from abc import ABC, abstractmethod

class FileHandler(ABC):

    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def write(self, data):
        pass

class TextFileHandler(FileHandler):
    def read(self):
        print("Reading data from a text file")

    def write(self, data):
        print(f"Writing '{data}' to a text file")

class BinaryFileHandler(FileHandler):
    def read(self):
        print("Reading data from a binary file")

    def write(self, data):
        print(f"Writing '{data}' to a binary file")

text_handler = TextFileHandler()
binary_handler = BinaryFileHandler()

text_handler.read()
text_handler.write("Hello")

binary_handler.read()
binary_handler.write(b"1010")