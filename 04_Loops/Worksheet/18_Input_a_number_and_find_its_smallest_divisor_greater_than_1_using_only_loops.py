"""
18. Input a number and find its smallest divisor greater than 1 (using only loops)
"""

n=int(input("enter the number: "))
for i in range(2,n+1):
    if(n%i==0):
        print(f"The smallest divisor {n} is ",i)
        break