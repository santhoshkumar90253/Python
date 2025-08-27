'''Python program to convert Set into Tuple and Tuple into Set
What changes when you go from set to tuple and back?'''
import ast
s = input("Enter the set:")
s=ast.literal_eval(s)
t = tuple(s)
print(t)
t = input("Enter the tuple:")
t=ast.literal_eval(t)
s = set(t)
print(s)
for i in s:
    print(i)