"""
6. Swap Two Numbers Without Using a Third Variable
Swap two variables’ values using a single line of code.
Sample Input: a = 15, b = 8
"""

a = int(input("enter a value : "))
b = int(input("enter b value : "))

a,b = b, a
print("a : ", a, "\nb : ", b)