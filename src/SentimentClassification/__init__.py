'''
SentimentClassifier.py
- `__init__(self)`: Initialises the `SentimentClassifier` class with configuration options and variables.
- `create_sentiment_classifier_df(self, hotel, label, df)`: Creates a DataFrame for sentiment analysis results for a specific hotel and label.
- `run_sentiment_classifier_df(self, label, n, hotel)`: Runs sentiment analysis on the DataFrame and retrieves the top `n` responses with the specified sentiment label.
- `run_sentiment_classifier(self, df)`: Runs the entire sentiment analysis process, including input collection and sentiment analysis results retrieval.

SentimentClassifierCore.py
- `__init__(self, df)`: Initialises the `SentimentClassifierCore` class with an input DataFrame `df`.
- `run_all_pipelines(self)`: Runs all the pipelines for preprocessing and sentiment analysis.
'''