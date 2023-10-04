'''
main.py
- `__init__(self)`: Initialises the `SurveyAnalysis` class.
- `intro(self)`: Returns an introduction message describing the purpose and techniques used in the survey analysis.
- `display_menu(self)`: Displays a menu to choose between different analysis techniques.
- `run_analysis(self)`: Runs the survey analysis based on the selected technique and user input.

DescriptiveStatistics.py
- `__init__(self, df)`: Initialises the `DescriptiveStatistics` class with a DataFrame `df`.
- `get_df_len(self)`: Returns the total number of survey responses in the DataFrame.
- `get_df_date_range(self)`: Returns the date range of data collection from the DataFrame.
- `get_df_head(self)`: Returns a sample of the DataFrame.
- `get_unique_user_count(self)`: Returns the number of unique users who submitted responses.
- `get_response_count_by_hotel(self)`: Returns the number of responses grouped by hotel.
- `get_top_response_count_by_country(self)`: Returns the number of responses grouped by the top three countries.
- `run_descriptive_statistics(self)`: Runs descriptive statistics on the DataFrame and returns the results as a formatted string.

utils.py
- `configure_pandas_display_options()`: Configures the display options for Pandas DataFrames. It sets the options to display all rows and columns without truncation, ensuring that you can see the full content of DataFrames.
- `filter_warnings()`: Suppresses Python warnings using the `warnings.filterwarnings("ignore")` statement. It prevents warning messages from being displayed in the console, which can be useful to maintain a cleaner and less noisy output during code execution.
- `setup_nltk()`: Sets up NLTK (Natural Language Toolkit) by downloading required resources. It specifically downloads the NLTK stopwords list and tokenisation data. It also customises the stopwords list by removing the words 'no' and 'not' from it, as these words are often important for sentiment analysis and should not be treated as stopwords.
'''