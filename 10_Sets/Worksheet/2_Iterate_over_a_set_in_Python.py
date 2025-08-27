'''Iterate over a set in Python
Story: You want to see every animal in your mini zoo, but the order doesn't matter.
The order may change every time. When is this helpful?'''
import ast
s=input("Enter the set:")
s=ast.literal_eval(s)
for i in s:
    print(i)