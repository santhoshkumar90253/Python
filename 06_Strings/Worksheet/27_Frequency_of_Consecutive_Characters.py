'''
27. Frequency of Consecutive Characters
Explanation: Count how many times each character repeats in sequence.
Input: "aabccddd"
Expected Output: {'a': 2, 'b': 1, 'c': 2, 'd': 3}
'''


def freq(s):
    if not s:
        return {}

    result = {}
    current_char = s[0]
    count = 1

    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1
        else:
            result[current_char] = count
            current_char = s[i]
            count = 1

    result[current_char] = count

    return result

s = "aabccddd"
output = freq(s)
print(output)