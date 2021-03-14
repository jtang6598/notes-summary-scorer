from reader import ReaderFactory
from tfidf import TFIDF


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

    if score < 0.06:
        score = 'bad'
    elif score < 0.14:
        score = 'okay'
    else:
        score = 'good'

    return {
        'statusCode': 200,
        'body': messages[score]
    }
