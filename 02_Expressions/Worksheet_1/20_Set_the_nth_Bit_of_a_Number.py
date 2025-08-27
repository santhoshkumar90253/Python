"""
20. Set the nth Bit of a Number
Write an expression that sets the nth bit of a given integer to 1 (leave other bits unchanged).
Sample Input: n = 9, bit_position = 3
"""

n=int(input("Enter the number: "))
pos=int(input("enter the position: "))

print(f"Before setting the bit {pos} position",bin(n),n)

x=n|(1<<pos)

print(f"After setting the bit {pos} poistion",bin(x),x)