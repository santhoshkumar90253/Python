'''Log Parser
 Covers: String manipulation and regular expressions
 Description: Extract and format key details (timestamp, severity, message) from each log entry.'''

import re

pattern = r"^(?P<timestamp>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3}) (?P<severity>[A-Z]+): \[(?P<module>.*?)\] - (?P<message>.*)$"


def pattern_extract(s):
    match=re.match(pattern,s)
    if match:
        return {'timestamp': match.group('timestamp'),'severity':match.group('severity'),'module':match.group('module'),'message':match.group('message')}
    else:
        return None
    
filename=input("Enter the log file name:")
try:
    file=open(filename,'r')
    content=file.readlines()
except FileNotFoundError:
    print("file does not exist!")
    exit()
n=1
for i in content:
    res=pattern_extract(i)
    print('log - ',n,' ',res)
    n+=1