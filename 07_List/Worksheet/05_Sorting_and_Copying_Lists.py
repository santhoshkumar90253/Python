'''
Sorting and Copying Lists

Log Session a list of numbers: [3, 1, 4, 2, 5].
Sort the list in ascending order.
Sort the list in descending order.
Copy the sorted list to a new list.
Print both lists to verify they are separate copies.'''


n=[3,2,1,5,4]
n.sort()
print(n)
n.sort(reverse=True)
print(n)
N=n.copy()
print(N)
print(n)