'''Count Vowels in a String Using Sets
Explanation: Find how many vowels (a, e, i, o, u) are in the string, using sets for efficiency.
Input: "education"
Expected Output: Vowels Count: 5'''
def count_vowels(s):
    s1={'a','e','i','o','u'}
    n=s.lower()
    c=0
    for i in n:
        if i in s1:
            c+=1
    return c
s=input("Enter the string: ")
print(f"The number of vowels are {count_vowels(s)}")