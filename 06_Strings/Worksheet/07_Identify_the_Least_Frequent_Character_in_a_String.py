'''Identify the Least Frequent Character in a String
Explanation: Find the character(s) that occur(s) the fewest times in a string.
Input: "statistics"
Expected Output: Least frequent character: 'a' '''

from collections import Counter

def least_freq(s):
    counts = Counter(s)
    return min(counts, key=counts.get)

s=input("Enter the string: ")
print(f"The character having least frequency {least_freq(s)}")