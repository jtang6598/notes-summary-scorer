from reader import DOCXReader, TXTReader


class ReaderFactory:

    def __init__(self):
        self.format_dict = {
            'docx': DOCXReader('').__class__,
            'txt': TXTReader('').__class__
        }

    def get(self, file):
        '''
        Returns an instance of a reader for the file's format
        :param file: File name, including format extension (e.g. .docx)
        :return: Reader instance
        '''
        format = file.split('.')[-1]
        return self.format_dict[format](file)

