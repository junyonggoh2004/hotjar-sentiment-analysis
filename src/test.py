import re
import subprocess
import multiprocessing
from datetime import datetime
import os
import pandas as pd

# # Get today's date and time
# now = datetime.now()

# # Format the date as 'ddmmyy'
# date_str = now.strftime('%d-%m-%Y')

# # Format the time as 'HHMMSS'
# time_str = now.strftime('%H-%M-%S%p')

# # Combine the date and time for the file name
# file_name = f"{date_str}_{time_str}"

# print(file_name)

# file_path ="C:\\Users\\Goh Jun Yong\\OneDrive\\Desktop\\Internship\HotJar Sentiment Analysis\\hotjar-sentiment-analysis\\data\\raw\\hotjar_survey_response_export_4078c75571a047239501417d2ebac864_2868694_821267_ASIN_Exit_Synxis.csv"
# modification_timestamp = os.path.getmtime(file_path)
# modification_datetime = datetime.fromtimestamp(modification_timestamp)
# print(modification_datetime)

