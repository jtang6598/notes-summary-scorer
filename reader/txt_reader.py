from reader.BaseReader import BaseReader


class TXTReader(BaseReader):

    def __init__(self, file):
        super().__init__(file)

    def read_lines(self):
        lines = None
        with open(self.file, 'rb') as f:
            lines = f.readlines()
        return lines
