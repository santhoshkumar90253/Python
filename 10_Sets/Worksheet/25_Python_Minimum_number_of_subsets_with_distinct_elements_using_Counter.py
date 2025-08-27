'''Python - Minimum number of subsets with distinct elements using Counter
'''
from collections import Counter
import ast
l=input("Enter the list:")
l=ast.literal_eval(l)

counts = Counter(l)
min_subsets = max(counts.values())

print("Minimum number of distinct-element subsets:", min_subsets)