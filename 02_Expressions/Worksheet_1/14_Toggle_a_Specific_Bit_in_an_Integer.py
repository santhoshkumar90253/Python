"""
14. Toggle a Specific Bit in an Integer
Given a number and a bit position, write an expression to toggle (flip) that bit.
Sample Input: n = 12, bit_position = 2
"""

n=int(input("Enter the n: "))
position=int(input("Enter the position: "))
x=n^(1<<position)
print(x)