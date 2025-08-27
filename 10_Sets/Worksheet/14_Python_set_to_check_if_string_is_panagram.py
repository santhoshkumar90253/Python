'''Python set to check if string is panagram
 Compare set of your letters with the alphabet set!'''

import string

def is_pangram(s):
    alphabet = set(string.ascii_lowercase)  
    s1 = set(s.lower())
    return alphabet.issubset(s1)


s = input("Enter the string: ")

if is_pangram(s):
    print("Yes, it's a pangram.")
else:
    print("No, it's not a pangram.")