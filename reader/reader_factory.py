from reader import DOCXReader, TXTReader


class ReaderFactory:

    def __init__(self):
        self.format_dict = {
            'docx': DOCXReader('').__class__,
            'txt': TXTReader('').__class__
        }

    def get(self, file):
        format = file.split('.')[-1]
        return self.format_dict[format](file)

