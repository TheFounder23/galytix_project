import pandas as pd
import gensim
from gensim.models import KeyedVectors

class embedings:
    def _init_(self, embedding_file, limit=1000000):
        self.temp = self.word_to_vec(embedding_file, limit)

    def word_to_vec(self, location, limit):
        temp = KeyedVectors.load2vec(location, binary=True, limit=limit)
        return temp

    def save_as_csv(self, output_file):
        self.temp.save_word2vec_format(output_file)

    def calculate_similarity(self, phr1, phr2, method='cosine'):
        pass

def main():
    embedding_file = '/siddharth/dtu books and notes/GoogleNews-vectors-negative300.bin'
    phrases_file = '/siddharth/dtu books and notes/phrases (1).csv'
    embedings = WordEmbedding(embedding_file)
    embedings.save_as_csv('vectors.csv')  

    phrases_df = pd.read_csv(phrases_file)
    for _, row in phrases_df.iterrows():
    embedding_file = '/siddharth/dtu books and notes/GoogleNews-vectors-negative300.bin'
    phrases_file = '/siddharth/dtu books and notes/phrases (1).csv'
    embedings = WordEmbedding(location)
    embedings.save_as_csv('vectors.csv') 
    print(f"Similarity between '{phr1}' and '{phr2}': {similarity}")

if _name_ == "_main_":
    main()
