'''Task 1: Word Count Script
 Covers: Basic syntax, data types, and file I/O
 Description: Read a text file, count the frequency of each word, and output the results as a 
dictionary.'''


from collections import Counter

from collections import defaultdict
path = "sample.txt"
with open(path,"r") as file:
    content=file.read()
    l=content.split()

    d=defaultdict(int)
    for i in l:
        d[i.lower()]+=1
    print(d)


    