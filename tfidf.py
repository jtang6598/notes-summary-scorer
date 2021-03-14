import pandas as pd
import numpy as np
from nltk.corpus import stopwords
import nltk

nltk.download('stopwords')
import re
from sklearn.feature_extraction.text import TfidfVectorizer


class TFIDF:

    def __init__(self):
        pass

    def find_similarity(self, corpus):

        documents_df = pd.DataFrame(corpus, columns=['documents'])

        # removing special characters and stop words from the text
        stop_words_l = stopwords.words('english')
        documents_df['documents_cleaned'] = documents_df.documents.apply(lambda x: " ".join(
            re.sub(r'[^a-zA-Z]', ' ', w).lower() for w in x.split() if
            re.sub(r'[^a-zA-Z]', ' ', w).lower() not in stop_words_l))

        tfidfvectorizer = TfidfVectorizer()
        tfidfvectorizer.fit(documents_df.documents_cleaned)
        tfidf_vectors = tfidfvectorizer.transform(documents_df.documents_cleaned)

        pairwise_similarities = np.dot(tfidf_vectors, tfidf_vectors.T).toarray()

        return self.most_similar(documents_df, 0, pairwise_similarities, 'Cosine Similarity')

    def most_similar(self, documents_df, doc_id, similarity_matrix, matrix):
        print(f'Document: {documents_df.iloc[doc_id]["documents"]}')
        print('\n')
        print('Similar Documents:')

        # get indices of similarity_matrix in order of decreasing score
        if matrix == 'Cosine Similarity':
            # greater cosine -> angle between vectors is small, so sort by decreasing cosine
            similar_ix = np.argsort(similarity_matrix[doc_id])[::-1]
        elif matrix == 'Euclidean Distance':
            # greater distance -> vectors are more different, so sort by increasing distance
            similar_ix = np.argsort(similarity_matrix[doc_id])

        # return second index -- first index (best match) is always similarity of document to itself
        return similarity_matrix[doc_id][similar_ix[1]]

tfidf = TFIDF()
print(tfidf.find_similarity(documents))
