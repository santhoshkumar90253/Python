'''Python - Program to accept the strings which contains all vowels
Can you check if the set of vowels is inside your word's letters?'''

def contains_all_vowels(s):
    vowels = set('aeiou')
    return vowels.issubset(set(s.lower()))

s = input("Enter a string: ")

if contains_all_vowels(s):
    print("The string contains all vowels.")
else:
    print("The string does NOT contain all vowels.")