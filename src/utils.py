import warnings
import subprocess
import re
import platform
from datetime import datetime
from colorama import Fore, Style

import nltk
import pandas as pd


# Windows-specific
def get_console_columns():
    os_name = platform.system()

    try:
        if os_name == 'Windows':
            cmd = ["mode"]
        elif os_name in ['Linux', 'Darwin']:
            cmd = ["stty", "-a"]
        else:
            print(f"{Fore.RED}UNSUPPORTED OPERATING SYSTEM{Style.RESET_ALL}")
            return None

        output = subprocess.check_output(
            cmd, stderr=subprocess.STDOUT, shell=os_name == 'Windows', text=True)

        if columns_match := re.search(r"Columns:\s+(\d+)", output):
            return int(columns_match[1])

    except subprocess.CalledProcessError:
        print("Unable to retrieve console window columns.")

    return None


def datetime_formatter():
    now = datetime.now()
    date_str = now.strftime('%d%m%Y')
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
