'''Nested Dictionaries
Nested dictionaries help organize complex data, like student records or configurations.
Represent student info with name, age, and a marks dictionary (math, english) using nested dictionaries for two students.
Access and print the english marks of 'Rahul' in:

        students = {'Rahul': {'age': 16, 'marks': {'math': 90, 'english': 88}},
        'Simran': {'age': 15, 'marks': {'math': 95, 'english': 92}}}
Expected Output: 88
For each student in the above students dictionary, print the name and all subject marks.
Add 'science': 93 to 'Simran''s marks in the nested dictionary.'''


students = {'Rahul': {'age': 16, 'marks': {'math': 90, 'english': 88}},
        'Simran': {'age': 15, 'marks': {'math': 95, 'english': 92}}}

print(students['Rahul']['marks']['english'])

for name, m in students.items():
    print(name,' -> ',m['marks'])
print("After modifying:")
students['Simran']['marks']['science']=93

for name, m in students.items():
    print(name,' -> ',m['marks'])