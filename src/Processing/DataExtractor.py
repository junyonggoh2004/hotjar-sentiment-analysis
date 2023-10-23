import os
import zipfile

from colorama import Fore, Style

from config import ARCHIVED_DATA_DIRECTORY, KEYWORDS_TO_UNZIP, SOURCE_DIRECTORY, TARGET_DIRECTORY, ZIP_EXTENSION


class DataExtractor:
    def __init__(self):
        pass

    def remove_existing_files(self):
        for file in os.listdir(TARGET_DIRECTORY):
            file_path = os.path.join(TARGET_DIRECTORY, file)
            if os.path.isfile(file_path):
                os.remove(file_path)
                print(
                    f"{Fore.LIGHTBLACK_EX}Successfully removed '{file}' from '{TARGET_DIRECTORY}'.{Style.RESET_ALL}")

    def process_zip_files(self):
        latest_files = {keyword: None for keyword in KEYWORDS_TO_UNZIP}

        zip_files = [file for file in os.listdir(
            SOURCE_DIRECTORY) if file.endswith(ZIP_EXTENSION)]

        for file in zip_files:
            for keyword in KEYWORDS_TO_UNZIP:
                if keyword in file:
                    file_path = os.path.join(SOURCE_DIRECTORY, file)
                    if latest_files[keyword] is None or os.path.getmtime(file_path) > os.path.getmtime(os.path.join(SOURCE_DIRECTORY, latest_files[keyword])):
                        latest_files[keyword] = file

        for latest_file in latest_files.values():
            if latest_file is not None:
                latest_file_path = os.path.join(
                    SOURCE_DIRECTORY, latest_file)
                with zipfile.ZipFile(latest_file_path, 'r') as zip_ref:
                    zip_ref.extractall(TARGET_DIRECTORY)
                    zip_ref.extractall(ARCHIVED_DATA_DIRECTORY)
                print(
                    f"{Fore.GREEN}Successfully unzipped '{latest_file}' to '{TARGET_DIRECTORY}{Style.RESET_ALL}'.")
            else:
                print(f"{Fore.RED}NO FILE FOUND{Style.RESET_ALL}")

    def run_extraction_pipeline(self):
        print()
        self.remove_existing_files()
        print()
        self.process_zip_files()
        print()
