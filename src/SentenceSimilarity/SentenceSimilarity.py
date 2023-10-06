import numpy as np
import pandas as pd
import time

from langdetect import detect
from sentence_transformers import util
from tqdm import tqdm

from config import HOTELS, SENTENCE_TRANSFORMER, TRANSLATOR, RESULTS_DIRECTORY
from utils import configure_pandas_display_options, filter_warnings, datetime_formatter


class SentenceSimilarity():
    def __init__(self):
        configure_pandas_display_options()
        filter_warnings()
        self.cos_sim = None
        self.cos_sim_matrix = []
        self.filtered_df = []
        self.sentence_similarity_df = None

    def compute_embeddings_and_similarity(self, hotel, df):
        self.filtered_df = df[df['Hotel'] == hotel] if hotel != 'all' else df
        embeddings = SENTENCE_TRANSFORMER.encode(
            np.array(self.filtered_df['clean_text']))
        self.cos_sim = util.cos_sim(embeddings, embeddings)
        return self.cos_sim

    def display_cos_sim_matrix(self):
        self.cos_sim_matrix = [
            (self.cos_sim[row][col], row, col)
            for row in range(len(self.cos_sim))
            for col in range(row + 1, len(self.cos_sim))
        ]
        self.cos_sim_matrix = sorted(
            self.cos_sim_matrix, key=lambda x: x[0], reverse=True)
        return self.cos_sim_matrix

    def create_sentence_similarity_df(self):
        self.filtered_df = self.filtered_df.reset_index(drop=True)
        original_text = self.filtered_df['What is stopping you from making a booking?']
        rows = []
        count = sum(
            len(original_text[col].split(" ")) > 1
            and len(original_text[row].split(" ")) > 1
            for score, row, col in self.cos_sim_matrix
        )

        with tqdm(total=count, desc="\nProcessing Responses", ascii='░█') as progress_bar:
            for score, row, col in self.cos_sim_matrix:
                if len(original_text[col].split(" ")) > 1 and len(original_text[row].split(" ")) > 1:
                    text1 = original_text[row]
                    text2 = original_text[col]
                    text1_language = detect(text1)
                    text2_language = detect(text2)
                    if text1_language != "en":
                        text1 = TRANSLATOR.translate(text1)

                    if text2_language != "en":
                        text2 = TRANSLATOR.translate(text2)

                    score_rounded = self.cos_sim[row][col].detach(
                    ).numpy().round(3)

                    rows.append([text1, text2, score_rounded])
                    progress_bar.update(1)

        self.sentence_similarity_df = pd.DataFrame(
            rows, columns=['Response 1', 'Response 2', 'Score'])

    def print_sentence_similarity_df(self, hotel, n):
        self.sentence_similarity_df = self.sentence_similarity_df.reset_index().drop('index',
                                                                                     axis=1)[:n]
        self.sentence_similarity_df.index.name = f"Most similar responses for {hotel}"
        self.sentence_similarity_df.to_csv(
            f"{RESULTS_DIRECTORY}\\Sentence Similarity\\top{n}_{hotel}_{datetime_formatter()}.csv", index=False)
        return self.sentence_similarity_df

    def run_sentence_similarity(self, df):
        print("\nEnter 'q' to return to the main menu.")

        while True:
            hotel = input(
                "\nEnter the hotel outlet (all (not recommended), ASIN, ASRS, ABKK): ")

            if hotel == 'q':
                return None
            elif hotel in HOTELS:
                break
            else:
                print("\nInvalid hotel outlet. Please enter a valid one.")

        self.compute_embeddings_and_similarity(hotel, df)
        self.display_cos_sim_matrix()
        self.create_sentence_similarity_df()

        sentence_similarity_df_len = len(self.sentence_similarity_df)
        print(
            f"\nThere is/are {sentence_similarity_df_len} pair(s) of responses from {hotel} to compare.")

        if sentence_similarity_df_len == 0:
            return None

        while True:
            if sentence_similarity_df_len == 1:
                time.sleep(0.5)
                result = self.print_sentence_similarity_df(hotel, sentence_similarity_df_len)
                print(result)
                break
            else:
                n = input(
                    "\nEnter the number of top pair(s) of responses to compare: ")

                if n == 'q':
                    return None

                try:
                    n = int(n)
                    if 1 <= n <= len(self.sentence_similarity_df):
                        time.sleep(0.2)
                        result = self.print_sentence_similarity_df(hotel, n)
                        print(result)
                        break
                    else:
                        print(
                            f"\nPlease enter a number between 1 and {sentence_similarity_df_len}.")
                except ValueError:
                    print("\nPlease enter a valid number or 'q' to quit.")
