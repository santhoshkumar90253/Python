'''
30. Count Frequency of Words in String (Short Form)
Explanation: Show how many times each word appears.
Input: "apple apple orange"
Expected Output: {'apple': 2, 'orange': 1}
'''

from collections import Counter

text = "apple apple orange"
freq = Counter(text.split())
print(dict(freq))