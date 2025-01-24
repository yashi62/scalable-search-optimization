import math
from database import Database
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class SearchEngine:
    def __init__(self):
        self.db = Database()
        self.documents = self.db.get_documents()
        self.vectorizer = TfidfVectorizer()
        self.document_matrix = self.vectorizer.fit_transform(self.documents['content'])
        self.page_size = 5

    def search(self, query, page=1):
        query_vector = self.vectorizer.transform([query])
        similarities = cosine_similarity(self.document_matrix, query_vector).flatten()
        self.documents['similarity'] = similarities

        ranked_results = self.documents.sort_values(by='similarity', ascending=False)
        total_results = ranked_results.shape[0]
        total_pages = math.ceil(total_results / self.page_size)
        start = (page - 1) * self.page_size
        end = start + self.page_size

        results = ranked_results.iloc[start:end].to_dict(orient='records')
        return results, total_pages
