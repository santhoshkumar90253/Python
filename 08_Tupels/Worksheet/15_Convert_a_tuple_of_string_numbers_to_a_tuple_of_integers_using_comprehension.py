'''
Description: Convert a tuple of string numbers to a tuple of integers using comprehension.
This is important for data cleaning and type conversion in real-world datasets.
Input: t = (("11", "22"), ("33", "44"))
Output: ((11, 22), (33, 44))
'''

t=(("11","22"),("33","44"),("55","66"))
t1=tuple(tuple(int(x) for x in m)for m in t)
print(t1)