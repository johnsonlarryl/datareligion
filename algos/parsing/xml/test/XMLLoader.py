import os


class XMLLoader:
    def loadFile(self, relative_path):
        os.path.dirname(__file__) + "/" + relative_path
        with open(relative_path, 'r') as file:
            return file.read().replace('\n', '')
