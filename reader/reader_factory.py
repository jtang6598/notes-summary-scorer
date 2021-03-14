from reader import PDFReader, DOCXReader, TXTReader


class ReaderFactory:

    def __init__(self):
        self.format_dict = {
            'pdf': PDFReader('').__class__,
            'docx': DOCXReader('').__class__,
            'txt': TXTReader('').__class__
        }

    def get(self, file):
        format = file.split('.')[1]
        return self.format_dict[format](file)

