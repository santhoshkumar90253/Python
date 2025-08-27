"""
2. Take an 8-bit register value and print if the **MSB** (most significant bit) is set or not.
Input: 0b10010010
Output: MSB set
"""

reg = input("Enter the 8 bit register value")
x=int(reg,2)
if x & 0b10000000:
    print("MSB set")
else:
    print("MSB not set")