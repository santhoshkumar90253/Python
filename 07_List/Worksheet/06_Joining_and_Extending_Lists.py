'''
Joining and Extending Lists

Log Session two lists: list1 = ["a", "b", "c"] and list2 = [1, 2, 3].
Concatenate the two lists into a new list.
Use the extend() method to add list2 to list1.
Print the final lists.
'''
a=['a','b','c']
b=[1,2,3]
c=a+b
a.extend(b)
print(a)
print(b)
print(c)