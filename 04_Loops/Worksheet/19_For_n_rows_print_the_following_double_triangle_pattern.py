"""
19. For n rows, print the following double triangle pattern
*
**
***
**
*
"""

n = int(input("Enter the number of rows (odd number): "))
mid = (n + 1) // 2  
for i in range(1, mid + 1):
    print('*' * i)
for i in range(mid - 1, 0, -1):
    print('*' * i)