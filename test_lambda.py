from lambda_function import lambda_handler


if __name__ == '__main__':
    event = {
        'files': ['testdoc.docx'],
        'notes': None,
        'summary': 'a guy went to the store, bought white pants, pooped in them, then they turned brown. he then went on his date in his new "khakis"'
    }
    print(lambda_handler(event, None))