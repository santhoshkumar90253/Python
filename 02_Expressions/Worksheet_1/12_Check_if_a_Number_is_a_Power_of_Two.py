"""
12. Check if a Number is a Power of Two
Write a single Boolean expression to check if a number is a power of two.
Sample Input: n = 32
"""

n=int(input("Enter the n: "))
x=n > 0 and ((n & (n - 1)) == 0)
print("powwer of 2"if(x) else"false")