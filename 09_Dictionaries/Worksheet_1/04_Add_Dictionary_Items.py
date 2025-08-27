'''Add Dictionary Items
Dynamic addition of new items allows for scalable and flexible data storage.
Add 'Bangalore': 12000000 to cities = {'Delhi': 18000000, 'Mumbai': 20000000}.
Add a key 'status' with value 'active' to user = {'name': 'Riya'} only if it doesn’t exist.
Given a list ['dog', 'cat', 'rabbit'], create a dictionary with words as keys and their lengths as values.
Expected Output: {'dog': 3, 'cat': 3, 'rabbit': 6}
Merge two dictionaries: d1 = {'x': 1} and d2 = {'y': 2}.
Expected Output: {'x': 1, 'y': 2}'''

cities = {'Delhi': 18000000, 'Mumbai': 20000000}
cities.update({'Bangalore':120000})
print("after updation cities:",cities)

user = {'name': 'Riya'}
if 'status' not in user.keys():
    user.update({'status':'active'})
    print(user)
else:
    print('status already present')
l=['dog', 'cat', 'rabbit']
d={}
for i in l:
    d[i]=len(i)
print("string as keys and length as values",d)
d1={'x':1}
d2={'y':2}
print(d1|d2)