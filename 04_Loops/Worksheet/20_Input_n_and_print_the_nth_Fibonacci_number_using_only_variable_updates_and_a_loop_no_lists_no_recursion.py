"""
20. Input n and print the nth Fibonacci number using only variable updates and a loop (no lists, no recursion).
"""

n=int(input("Enter the number: "))
i=0
x,y,z=0,1,0
while i<n:
    z=x+y
    x=y
    y=z
    i+=1
print(x)