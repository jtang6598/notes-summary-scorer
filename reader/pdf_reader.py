from reader.BaseReader import BaseReader
import PyPDF2


class PDFReader(BaseReader):

    def __init__(self, file):
        super().__init__(file)

    def read_lines(self):
        text = None
        with open(self.file, 'rb') as f:
            if __name__ == '__main__':
                pdfreader = PyPDF2.PdfFileReader(f)
                text = pdfreader
