'''
29. Minimum Rotations to Get the Original String
Explanation: Count the rotations needed for a string to return to its original form.
Input: "abcde"
Expected Output: 5
'''

def min_rotations(s):
    original = s
    n = len(s)
    rotated = s
    for i in range(1, n + 1):
        rotated = rotated[-1] + rotated[:-1]
        if rotated == original:
            return i

s = "abcde"
print(min_rotations(s))