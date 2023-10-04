from SentenceSimilarity.SentenceSimilarity import SentenceSimilarity


class SentenceSimilarityCore():

    def __init__(self, df):
        self.df = df
        self.sentence_similarity = SentenceSimilarity()

    def run_all_pipelines(self):
        self.df = self.sentence_similarity.run_sentence_similarity(self.df)
