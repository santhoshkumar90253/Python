''' Dictionaries
Dictionaries let you store and organize data using key-value pairs. They are fundamental for mapping, counting, and fast lookups.
Log Session a dictionary to store the roll numbers (as keys) and names (as values) for 3 students.
Sample Output: {101: 'Ravi', 102: 'Priya', 103: 'Amit'}
Suppose you write a dictionary with the same key twice. What value is stored?
Sample Input: d = {'x': 1, 'y': 2, 'x': 5}
Sample Output: {'x': 5, 'y': 2}
How can you check if the key 'fruit' exists in a dictionary called d?
Sample Input: d = {'fruit': 'apple', 'veg': 'carrot'}
Sample Output: True (when checked for 'fruit')
Count the frequency of each letter in the string "apple", store results in a dictionary, and print it.
Sample Input: "apple"
Sample Output: {'a': 1, 'p': 2, 'l': 1, 'e': 1}'''

import ast

d=input("Enter the dictionary roll number as keys and names as value:")
d=ast.literal_eval(d)
print("Dict:",d)
n=int(input("Enter the key to check if it exists or not:"))
if n in d.keys():
    print("Exists")
else:
    print("Not exists")
#count frequency
s=input("Enter the string:")
d={}
for i in s:
    d[i]=d.get(i,0)+1
print("Frequency of character:",d)