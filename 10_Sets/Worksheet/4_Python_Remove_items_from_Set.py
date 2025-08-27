'''Python - Remove items from Set'''

import ast
s=input("Enter the set:")
s=ast.literal_eval(s)
n=input("Enter the value to be deleted:")
s.remove(n)
print(s)