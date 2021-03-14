from reader import BaseReader
import PyPDF2


class PDFReader(BaseReader):

    def __init__(self, file):
        super().__init__(file)

    def read_text(self):
        text = []
        with open(self.file, 'rb') as f:
            pdfreader = PyPDF2.PdfFileReader(f)
            for page in pdfreader.pages:
                text.append(page.extractText())
        return ' '.join(text)
