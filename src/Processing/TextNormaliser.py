import contractions
import re
import unicodedata
from deep_translator.exceptions import TranslationNotFound
from joblib import Parallel, delayed

from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize
from textblob import TextBlob

from config import LEMMATISER, TRANSLATOR
from utils import setup_nltk


class TextNormaliser:
    def __init__(self):
        self.stopword_list = setup_nltk()
        self.translator = TRANSLATOR
        self.lemmatiser = LEMMATISER
        self.normalised_corpus = []

    def translate_text(self, text):
        try:
            text = self.translator.translate(
                text, src='auto', dest='en')
            return "" if text is None else text
        except TranslationNotFound:
            return text
    
    def correct_text(self, text):
        text = str(TextBlob(text).correct())
        return text

    def remove_accented_chars(self, text):
        text = unicodedata.normalize('NFKD', text).encode(
            'ascii', 'ignore').decode('utf-8', 'ignore')
        return text

    def remove_nonletters(self, text):
        pattern = r'[^a-zA-Z\s\']+'
        text = re.sub(pattern, '', text)
        text = re.sub(r'\s+', ' ', text)
        return text

    def expand_contractions(self, text):
        return contractions.fix(text)

    def convert_to_lowercase(self, text):
        text = text.lower()
        return text

    def remove_stopwords(self, text):
        tokens = text.split()
        filtered_words = [
            token for token in tokens if token.lower() not in self.stopword_list]
        return ' '.join(filtered_words)

    def lemmatise_text(self, text):
        pos_tags = {'NN': wordnet.NOUN, 'JJ': wordnet.ADJ,
                    'VB': wordnet.VERB, 'RB': wordnet.ADV}
        for pos_tag in pos_tags.values():
            tokens = word_tokenize(text)
            lemmatised_words = [self.lemmatiser.lemmatize(
                token, pos_tag) for token in tokens]
            text = ' '.join(lemmatised_words)
        return text

    def normalise_text(self, text, translate_text_f, correct_text_f, remove_accented_chars_f, remove_nonletters_f,
                       convert_to_lowercase_f, expand_contractions_f, remove_stopwords_f, lemmatise_text_f):
        if translate_text_f:
            text = self.translate_text(text)
        if correct_text_f:
            text = self.correct_text(text)
        if remove_accented_chars_f:
            text = self.remove_accented_chars(text)
        if remove_nonletters_f:
            text = self.remove_nonletters(text)
        if convert_to_lowercase_f:
            text = self.convert_to_lowercase(text)
        if expand_contractions_f:
            text = self.expand_contractions(text)
        if remove_stopwords_f:
            text = self.remove_stopwords(text)
        if lemmatise_text_f:
            text = self.lemmatise_text(text)
        return text

    def normalise_corpus(self, df,
                         translate_text_f=True,
                         correct_text_f=True,
                         remove_accented_chars_f=True,
                         remove_nonletters_f=True,
                         convert_to_lowercase_f=True,
                         expand_contractions_f=True,
                         remove_stopwords_f=True,
                         lemmatise_text_f=True):
        df = df.fillna('')
        
        def process_text(text):
            return self.normalise_text(
                text, translate_text_f, correct_text_f, remove_accented_chars_f, remove_nonletters_f,
                convert_to_lowercase_f, expand_contractions_f, remove_stopwords_f, lemmatise_text_f)
        
        self.normalised_corpus = Parallel(n_jobs=-1, verbose=11)(
            delayed(process_text)(text) for text in df['What is stopping you from making a booking?'])

        return self.normalised_corpus

    def insert_normalised_text_column(self, df):
        df['clean_text'] = self.normalise_corpus(df)
        return df