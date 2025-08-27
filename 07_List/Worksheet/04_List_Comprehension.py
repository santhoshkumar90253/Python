'''
List Comprehension

Log Session a list of fruits: "apple", "banana", "cherry", "kiwi", "mango".
Use list comprehension to create a new list containing fruits with the letter "a".
Convert all fruit names to uppercase using list comprehension.
Replace "banana" with "orange" using list comprehension.
'''

l = ["apple", "banana", "cherry", "kiwi", "mango"]
n = [i for i in l if 'a' in i]
print(n)
l = [i.upper() for i in l]
print(l)
l=["orange" if i=="BANANA" else i for i in l]
print(l)