from reader import ReaderFactory


if __name__ == '__main__':
    reader_factory = ReaderFactory()
    reader = reader_factory.get('testdoc.docx')
    print(reader.read_text())
