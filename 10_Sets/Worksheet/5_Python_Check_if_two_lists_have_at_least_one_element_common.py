'''Python - Check if two lists have at-least one element common    Which set operation shows what you both like?'''
import ast
list1 = input("Enter the list1:")
list2 = input("Enter the list2:")
list1=ast.literal_eval(list1)
list2=ast.literal_eval(list2)
set1 = set(list1)
set2 = set(list2)

if set1 & set2:  # or set1.intersection(set2)
    print("Yes, they have something in common:", set1 & set2)
else:
    print("No common elements.")