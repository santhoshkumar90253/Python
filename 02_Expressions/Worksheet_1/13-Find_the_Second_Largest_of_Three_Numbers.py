"""
13. Find the Second Largest of Three Numbers
Write an expression (no functions, no if) to get the second largest value among three numbers.
Sample Input: a = 20, b = 12, c = 18
"""

a=int(input("Enter the a: "))
b=int(input("Enter the b: "))
c=int(input("Enter the c: "))
print(a if (b > a > c or c > a > b) else b if (a > b > c or c > b > a)else c)