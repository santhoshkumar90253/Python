'''Python program to check whether a given string is Heterogram or not
Compare len(set(s)) and len(s).'''

import string

def is_heterogram(s):
    filtered = ''.join(ch.lower() for ch in s if ch.isalpha())
    return len(set(filtered)) == len(filtered)

s = input("Enter the string: ")

if is_heterogram(s):
    print("Yes, it's a heterogram!")
else:
    print("No, it's not a heterogram.")