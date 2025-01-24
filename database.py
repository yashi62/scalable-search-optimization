import pandas as pd

class Database:
    def __init__(self):
        self.documents = pd.read_csv('data/documents.csv')

    def get_documents(self):
        return self.documents
