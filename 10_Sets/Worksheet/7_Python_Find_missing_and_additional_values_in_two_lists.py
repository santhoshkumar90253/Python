
'''Python - Find missing and additional values in two lists   What set difference shows what you forgot?'''
import ast
list1 =input("Enter the list 1:")
list2 =input("Enter the list 2:")
list1=ast.literal_eval(list1)
list2=ast.literal_eval(list2)
s1 = set(list1)
s2 = set(list2)

missing = s1 - s2
additional = s2 - s1
print("Missing items:", missing)
print("Additional items:", additional)
