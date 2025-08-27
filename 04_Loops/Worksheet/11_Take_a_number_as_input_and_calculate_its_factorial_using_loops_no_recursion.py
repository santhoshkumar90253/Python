"""
11. Take a number as input and calculate its factorial using loops (no recursion).
"""

n=int(input("Enter the number:"))
f=1
n1=n
while n!=0:
    f=f*n
    n-=1
print(f"fatorial of {n1} is:",f)