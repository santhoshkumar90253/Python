''' Change Dictionaries
Updating dictionary values is needed when data changes during runtime.
Update the age of 'Anil' from 21 to 22 in this dictionary: ages = {'Anil': 21, 'Sunita': 20}.
Change multiple values at once in the dictionary: info = {'a': 10, 'b': 20} so that both 'a' and 'b' become 100.
Increase every salary in salaries = {'A': 20000, 'B': 30000} by 10%.
Sample Output: {'A': 22000.0, 'B': 33000.0}
Assign a value to a key that doesn't exist (e.g., add 'C': 25000 to salaries). What happens?'''

import ast
d=input("Enter the dictionary:")
d=ast.literal_eval(d)
print("Dict:",d)
s=input("Enter the key for updation:")
n=int(input("Enter the value for updation:"))
if s in d.keys():
    d[s]=n
    print('after modifying:',d)
else:
    print("Not found")

info = {'a': 10, 'b': 20}
info.update({'a':100})
print("info:",info)

salaries = {'A': 20000, 'B': 30000}
for i in salaries:
    salaries[i]*=1.10
print("After increasing 10%:",salaries)
salaries['c']=25000
print("After updation:",salaries)
salaries.update({'d':20000})
print("After updation:",salaries)