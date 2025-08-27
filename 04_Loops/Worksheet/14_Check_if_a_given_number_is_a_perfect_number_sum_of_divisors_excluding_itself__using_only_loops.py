"""
14. Check if a given number is a perfect number (sum of divisors excluding itself), using only loops
"""

n=int(input("Enter the number: "))
n1=n
sum=0
for i in range(1,n):
    if(n%i==0):
        sum+=i
if sum==n1:
    print(f"the number {n1} is perfect")
else:
     print(f"the number {n1} is not perfect")
     