"""
17. Check If a Number is a Multiple of 4 but Not of 8
Write an expression that is True only if a number is divisible by 4 but not by 8.
Sample Input: n = 12
"""

n=int(input("Enter the number: "))
x=(n%4==0) and (n%8!=0)
print("True"if(x) else "False")