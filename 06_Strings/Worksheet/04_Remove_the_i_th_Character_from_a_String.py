'''Remove the i-th Character from a String
Explanation: Remove the character at a given index in a string (starting from 0).
Input: String = "Python", i = 2
Expected Output: "Pythn"'''

def remove_ith(s,i):
    return s[:i]+s[i+1:]
s=input("Enter the string: ")
i=int(input("Enter the index position:"))
print(f"After removing {i} character from string: {remove_ith(s,i)}")