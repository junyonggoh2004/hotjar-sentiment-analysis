from collections import Counter
import time

from colorama import Fore, Style
import pandas as pd

from config import DASHBOARD_DATA_DIRECTORY, HOTELS, RESULTS_DIRECTORY
from utils import configure_pandas_display_options, datetime_formatter, filter_warnings


class TextTaggerSimplifier():

    def __init__(self):
        configure_pandas_display_options()
        filter_warnings()
        self.tag_word_dict = {}

    def simplify_pos_words(self, hotel, df):
        filtered_df = df if hotel in ['all', 'e'] else df[df['Hotel'] == hotel]

        # Create a list comprehension to extract and split NN, NNS, and NNP words
        noun_words = [word for NN, NNS, NNP in zip(filtered_df['NN'], filtered_df['NNS'], filtered_df['NNP'])
                      if NN or NNS or NNP
                      for word in f"{NN}, {NNS}, {NNP}".split(', ') if word]
        self.tag_word_dict['noun'] = noun_words

        # Create a list comprehension for various verb tags
        verb_words = [word for VBN, VBG, VBP, VBZ, VB, MD, VBD in zip(filtered_df['VBN'], filtered_df['VBG'], filtered_df['VBP'], filtered_df['VBZ'], filtered_df['VB'], filtered_df['MD'], filtered_df['VBD'])
                      if VBN or VBG or VBP or VBZ or VB or MD or VBD
                      for word in f"{VBN}, {VBG}, {VBP}, {VBZ}, {VB}, {MD}, {VBD}".split(', ') if word]
        self.tag_word_dict['verb'] = verb_words

        # Create a list comprehension for adverb tags
        adverb_words = [word for RB, RBS, WRB in zip(filtered_df['RB'], filtered_df['RBS'], filtered_df['WRB'])
                        if RB or RBS or WRB
                        for word in f"{RB}, {RBS}, {WRB}".split(', ') if word]
        self.tag_word_dict['adverb'] = adverb_words

        # Create a list comprehension for adjective tags
        adjective_words = [word for JJ, JJS in zip(filtered_df['JJ'], filtered_df['JJS'])
                           if JJ or JJS
                           for word in f"{JJ}, {JJS}".split(', ') if word]
        self.tag_word_dict['adjective'] = adjective_words

        return self.tag_word_dict

    def export_words_df(self):
        words_list = [item for sublist in self.tag_word_dict.values() for item in sublist]
        words_df = pd.DataFrame(
                words_list, columns=["Words"])

        words_df.to_csv(
                f"{DASHBOARD_DATA_DIRECTORY}\\text_tagger_data.csv", index=False)
        print(f"{Fore.LIGHTBLUE_EX}\nPOS-Tagging data uploaded to {DASHBOARD_DATA_DIRECTORY}.{Style.RESET_ALL}")

    def top_n_words(self, words_dict, word_category, n, hotel):
        word_list = words_dict[word_category]
        word_list_counter = Counter(word_list)
        most_common_words = word_list_counter.most_common(n)
        most_common_words_df = pd.DataFrame(
            most_common_words, columns=['Word', 'Count'])

        if n == 1:
            most_common_words_df.index.name = f'Top {word_category} used for {hotel}'
        else:
            most_common_words_df.index.name = f'Top {n} {word_category}s used for {hotel}'
        most_common_words_df.to_csv(
            f"{RESULTS_DIRECTORY}\\Text Tagger\\top{n}_{word_category}_{hotel}_{datetime_formatter()}.csv", index=False)
        return most_common_words_df

    def run_top_n_words(self, df):
        print()
        print("Enter 'q' to return to the main menu.")

        while True:
            hotel = input(
                "\nEnter the hotel outlet (all, ASIN, ASRS, ABKK) or 'e' to export data: ")
            if hotel == 'q':
                return None
            elif hotel in HOTELS or hotel == 'e':
                break
            else:
                print("\nInvalid hotel outlet. Please enter a valid one.")

        hotel_data = self.simplify_pos_words(hotel, df)
        if hotel == 'e':
            self.export_words_df()
        else:
            while True:
                word_category = input(
                    f"\nWARNING: The text tagger model used in this program may categorise adjectives as adverbs and vice versa.\nEnter the word category (noun, verb, adjective, adverb): ")
                if word_category == 'q':
                    return None
                elif word_category not in hotel_data.keys():
                    print("\nWord category does not exist.")
                else:
                    break

            unique_word_count = len(set(hotel_data[word_category]))
            print(
                f"\nThere is/are {unique_word_count} unique {word_category}(s) in {hotel}/'s responses.")

            while True:
                if unique_word_count == 0:
                    break
                elif unique_word_count == 1:
                    time.sleep(0.2)
                    return self.top_n_words(
                        hotel_data, word_category, unique_word_count, hotel
                    )
                else:
                    n = input("\nEnter the number of top word(s) to display: ")
                    if n == 'q':
                        return None
                    try:
                        n = int(n)
                        if n > unique_word_count or n < 1:
                            print(
                                f"\nPlease enter a number between 1 and {unique_word_count}.")
                        else:
                            result = self.top_n_words(
                                hotel_data, word_category, n, hotel
                            )
                            print(result)
                            break
                    except ValueError:
                        print("\nPlease enter a valid number or 'q' to quit.")
