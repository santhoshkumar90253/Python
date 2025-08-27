'''Find Close Matches for a String in a List
Explanation: Find list entries that are similar to the given word (helpful for typo correction).
Input: Target = "apple", List = ["apply", "apples", "ape", "maple"]
Expected Output: Close matches: ['apply', 'apples']'''
import ast
list=input("Enter the list:")
list=ast.literal_eval(list)
t=input("Enter the target:")
l=[]
for i in list:
    if t.startswith(i) or i.startswith(t):
        l.append(i)
print(l)