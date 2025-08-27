'''Python Set - Pairs of complete strings in two sets
Try making pairs and see if all alphabet letters are used together.'''

import string

alphabet = set(string.ascii_lowercase)
A = {"abcdefghijklm", "xyz", "helloworld"}
B = {"nopqrstuvwxyz", "abcdef", "python"}

pangram_pairs = []

for a in A:
    for b in B:
        combined = a + b
        if set(combined.lower()) >= alphabet:
            pangram_pairs.append((a, b))


print("Pangram pairs (together cover all letters):")
for pair in pangram_pairs:
    print(pair)