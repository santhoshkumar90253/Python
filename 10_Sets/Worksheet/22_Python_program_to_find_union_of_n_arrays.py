'''Python program to find union of n arrays'''

import ast
t=input("Enter the tuple:")
t=ast.literal_eval(t)

s = set()
for i in t:
    s |= set(i)  

print("All unique colors:", s)