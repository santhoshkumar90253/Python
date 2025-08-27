"""
8. Print a hollow square pattern of size n (n ≥ 3).
Example for n = 5:
*****
*   *
*   *
*   *
*****
"""
n = int(input("Enter the size of the square (n ≥ 3): "))
for i in range(n):
    if i == 0 or i == n - 1:
        print('*' * n)  
    else:
        print('*' + ' ' * (n - 2) + '*')