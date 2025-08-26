"""
11. Find the Largest of Three Numbers Using Only Expressions
Without using if, elif, or any function, write an expression to find the largest of three given numbers.
Sample Input: a = 14, b = 27, c = 19
"""

a=int(input("Enter the a: "))
b=int(input("Enter the b: "))
c=int(input("Enter the c: "))
print(a if a > b and a > c else b if b > c else c)