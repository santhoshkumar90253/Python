"""
2. Evaluate a Quadratic Expression
Given values for x, a, b, and c, write an expression to compute ax² + bx + c.
Sample Input: a = 2, b = 3, c = 4, x = 5
"""

x = int(input("Enter x value : "))
a = int(input("Enter a value : "))
b = int(input("Enter b value : "))
c = int(input("Enter c value : "))

print( (a * (x ** 2)) + (b * x) + c)