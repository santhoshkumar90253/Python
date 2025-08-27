'''Eliminate Duplicate Characters from a String
Explanation: Log Session a new string containing only the first occurrence of each character.
Input: "programming"
Expected Output: "progamin"'''
def eliminate_dup(s):
    print(s)
    seen=[]
    for i in s:
        if i not in seen:
            seen.append(i)
    return ''.join(seen)
s=input("Enter the string: ")
print(f"After removing the repeated character {eliminate_dup(list(s))}")