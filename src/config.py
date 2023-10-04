import os

from deep_translator import GoogleTranslator
import nltk
from nltk.stem import WordNetLemmatizer
from sentence_transformers import SentenceTransformer


# Constants and Configuration Settings
CSV_EXTENSION = '.csv'
# Defines the file extension for CSV files.

ZIP_EXTRENSION = ".zip"
# Defines the file extension for CSV files.

SOURCE_DIRECTORY = "C:\\Users\\Goh Jun Yong\\Downloads"
# SOURCE_DIRECTORY = "C:\\Users\\intern\\Downloads"
# Change it to your "Downloads" path
# Defines the directory containing the ZIP files to be unzipped

TARGET_DIRECTORY = "C:\\Users\\Goh Jun Yong\\OneDrive\\Desktop\\Internship\\HotJar Sentiment Analysis\\hotjar-sentiment-analysis\\data\\raw"
# TARGET_DIRECTORY = "L:\\Public Folder\\Dash Board\\JJ\\Digital Marketing\\HotJar Sentiment Analysis\\data\\raw"
# Defines the destination directory for unzipped files

DASHBOARD_DATA_DIRECTORY = "C:\\Users\\Goh Jun Yong\\OneDrive\\Desktop\\Internship\\HotJar Sentiment Analysis\\hotjar-sentiment-analysis\\data\\dashboard_data"
# DASHBOARD_DATA_DIRECTORY = "L:\\Public Folder\\Dash Board\\JJ\\Digital Marketing\\HotJar Sentiment Analysis\\data\\dashboard_data"
# Defines the destination directory for processed data

RESULTS_DIRECTORY = "C:\\Users\\Goh Jun Yong\\OneDrive\\Desktop\\Internship\\HotJar Sentiment Analysis\\hotjar-sentiment-analysis\\results"
# RESULTS_DIRECTORY = "L:\\Public Folder\\Dash Board\\JJ\\Digital Marketing\\HotJar Sentiment Analysis\\results"
# Defines the destination directory for analysis results

RAW_DATA_DIRECTORY = os.path.join(os.path.dirname(__file__), '..', 'data', 'raw')
# Specifies the path to the data folder where raw data files are stored.

KEYWORDS_TO_UNZIP = ["ASIN_Exit_Synxis",
                     "ABKK_Exit_Synxis", "ASRS_Exit_Synxis"]
# A list of keywords representing HotJar survey identifiers for data extraction

HOTELS = ["all", "ABKK", "ASIN", "ASRS"]
# A list of hotel identifiers, including "all" and specific hotel codes.

COLUMNS_TO_DROP = ["Number", "Hotjar User ID",
                   "Tags for: What is stopping you from making a booking?", "Device", "Browser", "OS", 'Source URL']
# Specifies a list of column names to be dropped or excluded from data analysis.

# Natural Language Processing Tools and Models
TRANSLATOR = GoogleTranslator(source="auto", target="en")
# Initializes a translator tool for translating text.

LEMMATISER = WordNetLemmatizer()
# Initializes a lemmatizer tool for word lemmatization.

NLTK_DICT = nltk.data.load('help/tagsets/upenn_tagset.pickle')
# Loads the NLTK dictionary, which provides information about part-of-speech tags.

SENTENCE_TRANSFORMER = SentenceTransformer('all-MiniLM-L6-v2')
# Initializes a Sentence Transformer model for sentence embeddings.

SENTIMENT_CLASSIFIER_MODEL = "nlptown/bert-base-multilingual-uncased-sentiment"
# Specifies the model used for sentiment classification.

SENTIMENT_CLASSIFIER_TASK = "sentiment-analysis"
# Defines the specific task associated with the sentiment classifier model.
