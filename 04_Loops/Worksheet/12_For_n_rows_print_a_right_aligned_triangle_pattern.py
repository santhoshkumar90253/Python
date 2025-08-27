"""
12. For n rows, print a right-aligned triangle pattern
    *
   **
  ***
 ****
*****
"""

n=int(input("Enter the number of rows:"))
for i in range(n):
    print(' ' *(n-i-1),end=(""))
    print("*" *(i+1))