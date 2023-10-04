from SentimentClassification.SentimentClassifier import SentimentClassifier


class SentimentClassifierCore():

    def __init__(self, df):
        self.df = df
        self.sentiment_analyser = SentimentClassifier()

    def run_all_pipelines(self):
        self.df = self.sentiment_analyser.run_sentiment_classifier(self.df)

