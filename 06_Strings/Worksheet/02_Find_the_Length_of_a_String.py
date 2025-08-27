'''
Find the Length of a String
Explanation: Count the total characters (including spaces) in a string.
Input: "hello world"
Expected Output: Length: 11
'''

def length(s):
    c=0
    for i in s:
        c+=1
    return c

s=input("Enter the string: ")
print(length(s))