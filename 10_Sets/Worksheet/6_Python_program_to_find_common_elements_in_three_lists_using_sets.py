'''Python program to find common elements in three lists using sets  Can you use set.intersection for this?'''

import ast
list1 =input("Enter the list 1:")
list2 =input("Enter the list 2:")
list3 = input("Enter the list 3:")
list1=ast.literal_eval(list1)
list2=ast.literal_eval(list2)
list3=ast.literal_eval(list3)

set1 = set(list1)
set2 = set(list2)
set3 = set(list3)

# Find common elements using set.intersection()
common = set1.intersection(set2, set3)  #set1&set2&set3

print("Common elements:", common)