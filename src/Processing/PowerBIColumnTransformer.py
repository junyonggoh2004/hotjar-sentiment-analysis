import os
import pandas as pd

from config import DASHBOARD_DATA_DIRECTORY
from colorama import Fore, Style


class PowerBIColumnTransformer:
    def __init__(self, df):
        self.df = df

    def return_dashboard_df(self):
        file_path = os.path.join(
            DASHBOARD_DATA_DIRECTORY, 'hotjar_survey_responses.csv')
        self.df.to_csv(file_path)
        print(f"{Fore.LIGHTBLUE_EX}Dashboard data uploaded to '{DASHBOARD_DATA_DIRECTORY}'.{Style.RESET_ALL}\n")

    def split_datetime_column(self):
        # Convert datetime column to datetime type
        self.df['Date Submitted'] = pd.to_datetime(self.df['Date Submitted'])
        # Extract date, day, and start of the hour
        self.df['Date'] = self.df['Date Submitted'].dt.strftime('%Y-%m-%d')
        self.df['Day'] = self.df['Date Submitted'].dt.strftime('%A')
        self.df['Hour'] = self.df['Date Submitted'].dt.floor(
            'H').dt.strftime('%I:%M:%S %p')
        self.df = self.df.drop(['Date Submitted'], axis=1)

    def run_transformer_pipeline(self):
        self.split_datetime_column()
        self.return_dashboard_df()
