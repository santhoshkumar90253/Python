'''
28. Rotate a String by k Positions
Explanation: Shift characters in the string to the right by k positions.
Input: String = "hello", k = 2
Expected Output: "lohel"
'''

def rotate(s,k):
    k=k%len(s)
    return s[-k:]+s[:-k]

s=input("Enter the string: ")
k=int(input("Enter the k value: "))
res = rotate(s,k)
print(res)