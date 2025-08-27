'''Custom Log Filter with Criteria
 • Concepts: Advanced string manipulation, regular expressions, file I/O, and dictionary 
usage.
• Description:
 Write a script that reads a log file and filters entries based on custom criteria—such as logs 
within a specific time range or containing a particular keyword pattern. Employ regex to 
accurately extract and process these elements.
 • Validation:
 Run the script on sample log data and confirm that the filtered output matches the specified 
criteria.'''

import re
from datetime import datetime

LOG_PATTERN = r"(?P<timestamp>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3}) (?P<level>[A-Z]+): (?P<message>.*)"

def is_within_time_range(log_time):
    return start_time <= log_time <= end_time

start_time_str = input("Enter start time (HH:MM): ").strip()   
end_time_str   = input("Enter end time (HH:MM): ").strip()     
keyword        = input("Enter keyword to search (leave blank to skip): ").strip()
filename       = input("Enter log file name: ").strip()
start_time = datetime.strptime(start_time_str, "%H:%M").time()
end_time   = datetime.strptime(end_time_str, "%H:%M").time()

with open(filename, "r") as file:
        for line in file:
            match = re.match(LOG_PATTERN, line)
            if match:
                timestamp_str = match.group("timestamp")
                message = match.group("message")
   
                log_dt = datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S,%f")
                log_time = log_dt.time()

                if is_within_time_range(log_time):
                    if keyword == "" or re.search(keyword, message, re.IGNORECASE):
                        print(line.strip())
