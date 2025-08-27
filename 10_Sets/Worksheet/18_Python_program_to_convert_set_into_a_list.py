'''Python program to convert set into a list'''

import ast
s = input("Enter the set:")
s=ast.literal_eval(s)
l=[]
for i in s:
    l.append(i)
print(l)
t = list(s)
print(t)