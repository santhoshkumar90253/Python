'''Python program to find the difference between two lists
Use set subtraction: A - B!'''

import ast
list1 =input("Enter the list 1:")
list2 =input("Enter the list 2:")
list1=ast.literal_eval(list1)
list2=ast.literal_eval(list2)
s1 = set(list1)
s2 = set(list2)

# Use set subtraction to find items in A but not in B
difference = s1 - s2

print("Items in A but not in B:", difference)