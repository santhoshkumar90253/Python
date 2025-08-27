'''Python program to get all subsets of given size of a set
Which Python library helps you make all teams?'''
from itertools import combinations
import ast
s=input("Enter the set:")
s=ast.literal_eval(s)
n=int(input("Enter the size:"))
teams =[ list(combinations(s, n))]

print("All possible teams of size", n)
for team in teams:
    print(team)