'''Find the size of a Set in Python
Story: You have a bag of unique toys. How many toys do you have?'''

import ast
s=input("Enter the set:")
s=ast.literal_eval(s)
print(s)
print(len(s))