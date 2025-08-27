"""
11. Enter a 16-bit value and print if parity (number of 1s) is even or odd.
Input: 0xAAAA
Output: Parity: Even
"""
n=input("Enter a 16 bit value:")
x=int(n,16)
print(x)
b=bin(x)
print("zero"if x==0 else "Even" if(b.count('1')%2==0)else "Odd")
