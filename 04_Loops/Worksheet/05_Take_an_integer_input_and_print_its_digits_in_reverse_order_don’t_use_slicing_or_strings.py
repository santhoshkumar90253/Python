"""
5. Take an integer input and print its digits in reverse order (don’t use slicing or strings)
"""

n = int(input("Enter an integer: "))
negative = n < 0
n = abs(n)

print("Reversed digits:")
while n > 0:
    digit = n % 10        
    print(digit, end=' ')
    n = n // 10         

if negative:
    print("\nOriginal number was negative")