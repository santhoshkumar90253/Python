'''Python - Intersection of two lists
How is this different if you use a list instead of a set?'''
import ast
list1=input("Enter the list 1:")
list2=input("Enter the list2:")
list1=ast.literal_eval(list1)
list2=ast.literal_eval(list2)

common = list(set(list1) & set(list2))
print("Common elements:", common)