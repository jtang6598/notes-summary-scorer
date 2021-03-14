from reader import BaseReader
from docx import Document


class DOCXReader(BaseReader):

    def __init__(self, file):
        super().__init__(file)

    def read_text(self):
        document = Document(self.file)
        text = []
        # docx Document splits doc by pages; get text from each page
        for par in document.paragraphs:
            text.append(par.text)
        # aggregate all text from the document
        return ' '.join(text)
