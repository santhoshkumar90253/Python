"""
6. Check if the input number reads the same backward as forward, using only loops and arithmetic
"""

n = int(input("Enter an integer: "))
negative = n < 0
n = abs(n)
s=0
original=n
while n > 0:
    digit = n % 10        
    s=s*10+digit
    n = n // 10   
    
if s==original:
    print("True")
else:
    print("False")
if negative:
    print("\nOriginal number was negative")