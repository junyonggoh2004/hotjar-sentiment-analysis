import re
import subprocess
import multiprocessing
from datetime import datetime

# Get today's date and time
now = datetime.now()

# Format the date as 'ddmmyy'
date_str = now.strftime('%d-%m-%Y')

# Format the time as 'HHMMSS'
time_str = now.strftime('%H-%M-%S%p')

# Combine the date and time for the file name
file_name = f"{date_str}_{time_str}"

print(file_name)
