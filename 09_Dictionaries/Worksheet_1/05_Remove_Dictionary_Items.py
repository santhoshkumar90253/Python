'''Remove Dictionary Items
Sometimes, you need to clean up or adjust your dictionary as data changes.
Remove key 'math' from marks = {'math': 80, 'science': 85} using del.
Use .pop() to remove 'name' from info = {'name': 'Amit', 'city': 'Pune'} and print the value removed.
Remove all items from the dictionary: d = {'x': 1, 'y': 2}.
Write a program to remove key 'z' from d = {'x': 1, 'y': 2} only if it exists.
Expected Output: If not found, print 'Key not found'.'''


marks = {'math': 80, 'science': 85}
del marks['math']
print("After deleting 'math':", marks)

info = {'name': 'Amit', 'city': 'Pune'}
removed_value = info.pop('name')
print("Removed value using pop():", removed_value)
print("After pop():", info)

d1 = {'x': 1, 'y': 2}
d1.clear()
print("After clearing all items:", d1)

d2 = {'x': 1, 'y': 2}
if 'z' in d2:
    del d2['z']
else:
    print("Key not found")