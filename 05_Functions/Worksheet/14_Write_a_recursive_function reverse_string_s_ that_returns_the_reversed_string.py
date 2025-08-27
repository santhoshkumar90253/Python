'''Write a recursive function reverse_string(s) that returns the reversed string'''

def reverse_string(s):
    if len(s)<=1:
        return s
    return s[-1]+reverse_string(s[:-1])
s=input("Enter the string: ")
print(f"After reversing {reverse_string(s)}")