from reader import BaseReader


class TXTReader(BaseReader):

    def __init__(self, file):
        super().__init__(file)

    def read_text(self):
        text = None
        with open(self.file, 'r') as f:
            text = f.read()
        return text
