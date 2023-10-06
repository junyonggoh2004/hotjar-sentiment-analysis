'''
DataExtractor.py
- `__init__(self)`: Initialises the DataExtractor class.
- `remove_existing_files(self)`: Removes existing files from the target directory.
- `process_zip_files(self)`: Processes ZIP files and extracts the latest file by each keyword into the 'raw' and 'archive' directories.
- `run_extraction_pipeline(self)`: Runs the data extraction pipeline.

DataProcessor.py
- `__init__(self)`: Initialises the DataProcessor class.
- `get_df(self)`: Returns the processed dataframe.
- `load_and_concat_dataframes(self)`: Loads and concatenates dataframes from CSV files, associating each entry with a specific hotel.
- `drop_columns(self)`: Drops unnecessary columns from the dataframe.
- `run_preprocessing_pipeline(self)`: Runs the data preprocessing pipeline, including loading, concatenating, and column dropping, resulting in the processed dataframe.

PowerBIColumnTransformer.py
- __init__(self, df): Initializes the PowerBIColumnTransformer with a DataFrame.
- return_dashboard_df(self): Saves the processed DataFrame to a CSV file for use in PowerBI Dashboard.
- split_datetime_column(self): Splits a datetime column into date, day, and hour columns.
- run_transformer_pipeline(self): Runs the column transformation pipeline.

TextNormaliser.py
- `__init__(self)`: Initialises the TextNormaliser class.
- `translate_text(self, text)`: Translates text to English.
- `correct_text(self, text)`: Corrects the spelling and grammar of text.
- `remove_accented_chars(self, text)`: Removes accented characters from text.
- `remove_nonletters(self, text)`: Removes non-alphabetical characters from text.
- `expand_contractions(self, text)`: Expands contractions in text.
- `convert_to_lowercase(self, text)`: Converts text to lowercase.
- `remove_stopwords(self, text)`: Removes stopwords from text.
- `lemmatise_text(self, text)`: Lemmatises words in text.
- `normalise_corpus(self, df, ...)`: Normalises the text corpus in the given dataframe using a set of specified text preprocessing methods.
- `insert_normalised_text_column(self, df)`: Inserts the normalised text as a new column in the dataframe.
'''
