import nltk
import pandas as pd

from config import NLTK_DICT


class TextTagger:
    def __init__(self):
        self.nltk_dict = NLTK_DICT

    def load_configure_nltk(self):
        # Define the list of keys to remove
        keys_to_remove = ['--', ':', '(', ')', '.', ',', '``', '$', 'TO', 'WP', 'UH',
                          'PRP', 'WP$', 'NNPS', 'PRP$', 'WDT', 'RBR', 'RP', 'JJR', 'PDT', 'EX', 'SYM']

        # Remove unwanted keys from the NLTK dictionary
        for key in keys_to_remove:
            self.nltk_dict.pop(key, None)

    def prepare_tag_word_df(self, df):
        tag_word_df = pd.DataFrame(
            {tag: [''] * len(df) for tag in self.nltk_dict.keys()}, dtype='object')

        # Insert the 'clean_text' column from the input DataFrame
        tag_word_df.insert(0, 'clean_text', df['clean_text'])
        df = df.merge(tag_word_df, on='clean_text',
                      how='inner').drop_duplicates().reset_index(drop=True)

        return df

    def populate_df_by_tag(self, df):
        sentences = df['clean_text'].tolist()
        for row, sentence in enumerate(sentences):
            lemmatised_words = sentence.split(" ")
            data = nltk.pos_tag(lemmatised_words)
            for token, tag in data:
                if token not in df.at[row, tag]:
                    if df.at[row, tag] == '':
                        df.at[row, tag] = token
                    else:
                        df.at[row, tag] += f', {token}'
        return df

    def run_tagger_pipeline(self, df):
        self.load_configure_nltk()
        df = self.prepare_tag_word_df(df)
        df = self.populate_df_by_tag(df)

        return df
