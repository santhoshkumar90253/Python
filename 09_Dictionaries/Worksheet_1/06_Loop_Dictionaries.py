'''Loop Dictionaries
Iterating over dictionaries lets you process or filter keys and values.
Loop and print all keys in d = {'a': 10, 'b': 20, 'c': 30}.
Loop and print all values in the same dictionary.
Loop and print each key and its value together.
Print only the subjects with marks above 60 from scores = {'math': 75, 'science': 55, 'english': 82}.
Sample Output:
math
english'''


d = {'a': 10, 'b': 20, 'c': 30}

print("Keys:")
for key in d:
    print(key)

print("Values:")
for value in d.values():
    print(value)

print("Key-Value Pairs:")
for key, value in d.items():
    print(key, "->", value)

scores = {'math': 75, 'science': 55, 'english': 82}
print("Subjects with marks above 60:")
for subject, mark in scores.items():
    if mark > 60:
        print(subject)