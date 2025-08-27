''' Write a function calculate(a, b) that returns both the sum and difference of a and b'''

def calculate(a, b):
    sum = a + b
    diff = a - b
    return sum, diff
a=int(input("Enter the number 1: "))
b=int(input("Enter the number 2: "))
x, y = calculate(a, b)
print("Sum:", x)
print("Difference:", y)