'''Python - Maximum and Minimum in a Set'''

import ast
s=input("Enter the set:")
s=ast.literal_eval(s)
s=list(s)
maximum=minimum=s[0]
for i in s:
    if i>maximum:
        maximum=i
    if i<minimum:
        minimum=i
print("max:",maximum,"min:",minimum)