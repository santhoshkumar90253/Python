"""
7. Ask for two numbers and compute their Greatest Common Divisor (GCD) using repeated subtraction or division with loops.
"""

n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
a = abs(n1)
b = abs(n2)
while a != b:
    if a > b:
        a = a - b
    else:
        b = b - a

print("GCD is:", a)
a = abs(n1)
b = abs(n2)
while b != 0:
    temp = b
    b = a % b
    a = temp

print("GCD is:", a)