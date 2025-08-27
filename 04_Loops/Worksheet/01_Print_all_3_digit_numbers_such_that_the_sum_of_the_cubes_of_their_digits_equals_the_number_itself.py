"""
1. Print all 3-digit numbers such that the sum of the cubes of their digits equals the number itself.
Example: 153 → 1³ + 5³ + 3³ = 153
"""
for i in range(100,1000):
    j=i
    s=0
    while j!=0:
        m = j%10
        s = s + (m**3)
        j//=10
    if i==s:
        print(i)