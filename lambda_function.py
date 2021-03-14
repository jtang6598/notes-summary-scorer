from reader import ReaderFactory
from tfidf import TFIDF
from requests_toolbelt.multipart import decoder


messages = {
    'good': 'Nice summary! You sure know your stuff!',
    'okay': "You're on your way to success, but you could use some more studying!",
    'bad': 'Oof, you should really consider hitting the books....'
}


def lambda_handler(event, context):
    reader_factory = ReaderFactory()
    notes = []

    if event['files']:
        for file in event['files']:
            reader = reader_factory.get(file)
            notes.append(reader.read_text())

    if event['notes']:
        notes.append(event['notes'])

    notes = ' '.join(notes)

    tfidf = TFIDF()
    score = tfidf.find_similarity([notes, event['summary']])
    level = None

    if score < 0.06:
        level = 'bad'
    elif score < 0.14:
        level = 'okay'
    else:
        level = 'good'

    return {
        'statusCode': 200,
        'body': {
            'score': score,
            'message': messages[level]
        }
    }

def lambda_new(event, context):
    content_type_header = event['headers']['content-type'] + '; boundary=' + event['body'].split('\r')[0].split('-')[-1]
    # content_type_header = event['headers']['content-type'] + '; boundary=----WebKitFormBoundaryhkPBzaCCH5WTm3qe'

    body = event['body'].encode()

    response = ''
    for part in decoder.MultipartDecoder(body, content_type_header).parts:
        response += part.text + "\n"

    return {
        'statusCode': 200,
        'body': response
    }
