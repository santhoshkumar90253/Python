''' Task 2: Log Filter
 Covers: File I/O and exception handling
 Description: Process a log file to extract lines containing "ERROR" and write them to a new file, 
handling missing files gracefully.'''

filename=input("Enter the filename:")

try:
    file=open(filename,"r")
    content=file.readlines()
except FileNotFoundError:
    print("File not found!")
    exit()

file1=open("Error_line.txt",'w')
for i in content:
    if 'ERROR' in i:
        file1.write(i)

print("line containing error is written successfully")