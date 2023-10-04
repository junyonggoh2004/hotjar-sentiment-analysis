import pandas as pd
import time
import string
import datetime

from langdetect import detect
from transformers import pipeline
from tqdm import tqdm

from config import HOTELS, SENTIMENT_CLASSIFIER_MODEL, SENTIMENT_CLASSIFIER_TASK, TRANSLATOR, RESULTS_DIRECTORY
from utils import configure_pandas_display_options, filter_warnings, datetime_formatter


class SentimentClassifier():

    def __init__(self):
        configure_pandas_display_options()
        filter_warnings()
        self.filtered_df = None
        self.hotels = HOTELS
        self.model = SENTIMENT_CLASSIFIER_MODEL
        self.task = SENTIMENT_CLASSIFIER_TASK
        self.sentiment_classifier_df = None
        self.translator = TRANSLATOR

    def create_sentiment_classifier_df(self, hotel, label, df):
        sentiment_pipeline = pipeline(self.task, model=self.model)
        label_dict = {
            '5 stars': 'positive',
            '4 stars': 'positive',
            '3 stars': 'neutral',
            '2 stars': 'negative',
            '1 star': 'negative',
        }

        def contains_only_punctuation(text):
            return all(char in string.punctuation or char.isspace() for char in text)

        self.filtered_df = df if hotel == 'all' else df[df['Hotel'] == hotel]
        total_iterations = len(self.filtered_df)

        with tqdm(total=total_iterations, desc="\nProcessing Responses", ascii='░█') as progress_bar:
            rows = []
            for text in self.filtered_df['What is stopping you from making a booking?']:
                sentiment = sentiment_pipeline(text)[0]
                confidence = round(sentiment['score'] * 100, 1)
                sentiment_label = label_dict[sentiment['label']]

                if text is not None and not contains_only_punctuation(text):
                    text_language = detect(text)
                    if text_language != "en":
                        text = self.translator.translate(text)
                        rows.append(
                            [f"{text}", f"{confidence}%", sentiment_label])
                    else:
                        rows.append([text, f"{confidence}%", sentiment_label])

                progress_bar.update(1)

        self.sentiment_classifier_df = pd.DataFrame(
            rows, columns=['Response', 'Confidence', 'Label'])
        self.sentiment_classifier_df = self.sentiment_classifier_df[
            self.sentiment_classifier_df['Label'] == label]

        return self.sentiment_classifier_df

    def run_sentiment_classifier_df(self, label, n, hotel):
        if not self.sentiment_classifier_df.empty:
            self.sentiment_classifier_df = self.sentiment_classifier_df.sort_values(
                by="Confidence", ascending=False).reset_index(drop=True)[:n]

            if n == 1:
                index_name = f'Top {label} used for {hotel}'
            else:
                index_name = f'Top {n} {label} responses for {hotel}'

            self.sentiment_classifier_df.index.name = index_name
            self.sentiment_classifier_df.to_csv(
                f"{RESULTS_DIRECTORY}\\Sentiment Classification\\top{n}_{label}_{hotel}_{datetime_formatter()}.csv", index=False)
            return self.sentiment_classifier_df
        else:
            print(f"There are no {label} responses.")

    def run_sentiment_classifier(self, df):
        print("\nEnter 'q' to return to the main menu.")

        # Ask for user input for hotel name
        while True:
            hotel = input("\nEnter the hotel outlet (all, ASIN, ASRS, ABKK): ")
            if hotel == 'q':
                return None
            elif hotel in self.hotels:
                break
            else:
                print("\nInvalid hotel outlet. Please enter a valid one.")

        # Ask for user input for sentiment label
        while True:
            label = input(
                "\nEnter the sentiment label (positive, neutral, negative): ")
            if label == 'q':
                return None
            elif label in ['positive', 'neutral', 'negative']:
                break
            else:
                print("\nSentiment label does not exist.")

        self.create_sentiment_classifier_df(hotel, label, df)
        sentiment_classifier_df_len = len(self.sentiment_classifier_df)

        print(
            f"\nThere is/are {sentiment_classifier_df_len} {label} response(s) from {hotel}.")

        # Ask for the top n most common words
        while True:
            if sentiment_classifier_df_len == 0:
                break
            elif sentiment_classifier_df_len == 1:
                time.sleep(0.5)
                result = self.run_sentiment_classifier_df(
                    label, sentiment_classifier_df_len, hotel)
                print(result)
                break
            else:
                n = input(f"\nEnter the number of top {label} response(s): ")
                if n == 'q':
                    return None  # Exit the function if 'q' is entered
                try:
                    n = int(n)
                    if n > sentiment_classifier_df_len or n < 1:
                        print(
                            f"\nPlease enter a number between 1 and {sentiment_classifier_df_len}.")
                    else:
                        time.sleep(0.2)
                        result = self.run_sentiment_classifier_df(
                            label, n, hotel)
                        print(result)
                        break
                except ValueError:
                    print("\nPlease enter a valid number or 'q' to quit.")
                print()
