"""
10. Input a number and count how many digits it contains, using only arithmetic and loops.
"""

n = int(input("Enter an integer: "))
negative = n < 0
n = abs(n)
c=0
while n > 0:
    digit = n % 10        
    c+=1
    n = n // 10         

print(c)