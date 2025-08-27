"""
2. For a given number, print its multiplication table from 1 to 10, but don’t use the * operator.
"""

num = int(input("Enter a number: "))
for i in range(1, 11):
    product = 0
    for _ in range(i):
        product += num
    print(f"{num} x {i} = {product}")