"""
4. For a given number of rows, print the following number pyramid pattern
1
1 2
1 2 3
...
1 2 ... n
"""

r=int(input("Enter number of rows: "))
for i in range(1,r+1):
    for j in range(i):
        print(j+1,end=" ")
    print()