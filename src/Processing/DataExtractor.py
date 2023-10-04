import os

from colorama import Fore, Style
import zipfile

from config import ZIP_EXTRENSION, SOURCE_DIRECTORY, TARGET_DIRECTORY, KEYWORDS_TO_UNZIP


class DataExtractor:
    def __init__(self):
        self.ZIP_EXTENSION = ZIP_EXTRENSION
        self.SOURCE_DIRECTORY = SOURCE_DIRECTORY
        self.TARGET_DIRECTORY = TARGET_DIRECTORY
        self.KEYWORDS_TO_UNZIP = KEYWORDS_TO_UNZIP

    def remove_existing_files(self):
        for file in os.listdir(self.TARGET_DIRECTORY):
            file_path = os.path.join(self.TARGET_DIRECTORY, file)
            if os.path.isfile(file_path):
                os.remove(file_path)
                print(
                    f"{Fore.LIGHTBLACK_EX}Successfully removed '{file}' from '{self.TARGET_DIRECTORY}'.{Style.RESET_ALL}")

    def process_zip_files(self):
        latest_files = {keyword: None for keyword in self.KEYWORDS_TO_UNZIP}

        zip_files = [file for file in os.listdir(
            self.SOURCE_DIRECTORY) if file.endswith(self.ZIP_EXTENSION)]

        for file in zip_files:
            for keyword in self.KEYWORDS_TO_UNZIP:
                if keyword in file:
                    file_path = os.path.join(self.SOURCE_DIRECTORY, file)
                    if latest_files[keyword] is None or os.path.getmtime(file_path) > os.path.getmtime(os.path.join(self.SOURCE_DIRECTORY, latest_files[keyword])):
                        latest_files[keyword] = file

        for latest_file in latest_files.values():
            if latest_file is not None:
                latest_file_path = os.path.join(
                    self.SOURCE_DIRECTORY, latest_file)
                with zipfile.ZipFile(latest_file_path, 'r') as zip_ref:
                    zip_ref.extractall(self.TARGET_DIRECTORY)
                print(
                    f"{Fore.GREEN}Successfully unzipped '{latest_file}' to '{self.TARGET_DIRECTORY}{Style.RESET_ALL}'.")
            else:
                print(f"{Fore.RED}NO FILE FOUND{Style.RESET_ALL}")

    def run_extraction_pipeline(self):
        print()
        self.remove_existing_files()
        print()
        self.process_zip_files()
        print()
