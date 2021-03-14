from reader.BaseReader import BaseReader
from docx import Document


class DOCXReader(BaseReader):

    def __init__(self, file):
        super().__init__(file)

    def read_lines(self):
        document = Document(self.file)
        text = []
        for par in document.paragraphs:
            text.append(par.text)
        return text
