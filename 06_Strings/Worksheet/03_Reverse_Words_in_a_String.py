'''Reverse Words in a String
Explanation: Reverse the order of words in a sentence, not the letters.
Input: "I love Python"
Expected Output: "Python love I"'''

def reverse_words(s):
    return ' '.join(s.split()[::-1])

s = input("Enter the string: ")
reversed_string = reverse_words(s)
print(reversed_string)
