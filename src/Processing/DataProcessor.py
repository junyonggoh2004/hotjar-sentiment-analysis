import os
import pandas as pd

from config import COLUMNS_TO_DROP, CSV_EXTENSION, RAW_DATA_DIRECTORY, HOTELS


class DataProcessor:
    def __init__(self):
        self.hotels = HOTELS
        self.df = None

    def load_and_concat_dataframes(self):
        dfs = []

        # Loop through files in RAW_DATA_DIRECTORY
        for file_path in os.listdir(RAW_DATA_DIRECTORY):
            if file_path.endswith(CSV_EXTENSION):
                file_full_path = os.path.join(RAW_DATA_DIRECTORY, file_path)
                # Check if the file is empty
                if os.path.getsize(file_full_path) > 0:
                    df = pd.read_csv(file_full_path)
                    # Check for hotel keyword in file_path
                    for hotel in self.hotels:
                        if hotel in file_path:
                            df['Hotel'] = hotel

                    # Check if 'text' column contains any of the specified words
                    remove_hi = df[~df['What is stopping you from making a booking?'].str.lower().isin([
                        'hello', 'hi'])]
                    dfs.append(remove_hi)

        if dfs:
            self.df = pd.concat(dfs, axis=0, ignore_index=True)

    def drop_columns(self):
        if self.df is not None:
            self.df = self.df.drop(columns=COLUMNS_TO_DROP, axis=1)
        return self.df

    def run_processing_pipeline(self):
        self.load_and_concat_dataframes()
        if self.df is None:
            return None, True
        self.drop_columns()
        return self.df, False
