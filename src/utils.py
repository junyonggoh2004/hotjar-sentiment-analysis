import warnings
import subprocess
import re
from datetime import datetime

import nltk
import pandas as pd

# Windows-specific


def get_console_columns():
    try:
        # Run the "mode" command and capture its output
        output = subprocess.check_output(
            ["mode"], stderr=subprocess.STDOUT, shell=True, text=True)

        if columns_match := re.search(r"Columns:\s+(\d+)", output):
            return int(columns_match[1])
        return None

    except subprocess.CalledProcessError:
        # Handle errors if the "mode" command fails
        print("Unable to retrieve console window columns.")
        return None


def datetime_formatter():
    now = datetime.now()
    # Format the date as 'dd-mm-yyyy'
    date_str = now.strftime('%d%m%Y')

    # Format the time as 'hh-mm-ss'
    time_str = now.strftime('%H%M%S')

    return f"{date_str}_{time_str}"


def configure_pandas_display_options():
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_colwidth', None)


def filter_warnings():
    warnings.filterwarnings("ignore")


def setup_nltk():
    nltk.download('stopwords')
    nltk.download('wordnet')
    nltk.download('tagsets')
    nltk.download('averaged_perceptron_tagger')
    nltk.download('punkt')
    stopword_list = nltk.corpus.stopwords.words('english')
    stopword_list.remove('no')
    stopword_list.remove('not')
    return stopword_list
