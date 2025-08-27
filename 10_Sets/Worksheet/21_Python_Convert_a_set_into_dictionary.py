'''Python - Convert a set into dictionary
Try using enumerate() to give each item a number.'''
import ast
s1 = input("Enter the set:")
s1=ast.literal_eval(s1)

my_dict = {i: item for i, item in enumerate(s1)}

print("Dictionary from set:", my_dict)