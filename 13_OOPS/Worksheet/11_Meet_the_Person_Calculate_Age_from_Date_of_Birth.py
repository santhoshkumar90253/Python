'''
11. Meet the Person: Calculate Age from Date of Birth
Scenario:
Log Session a birthday tracker! Determine someone’s age from their date of birth.

What you’ll learn:
Handling dates and calculating with them
Real-world use of classes

Task:
Make a Person class and compute age.

Example:
For a person born on 2000-05-25 (today is 2025-05-25):
'''

class person:
    def __init__(self,name,born,today):
        self.name,self.born,self.today=name,born,today

    def compute(self):
        x,y=int(self.today[6:]),int(self.born[6:])
        return x-y

s=person("SUNIL","17-06-2001","03-07-2025")
print(f"{s.name} is {s.compute()} Years Old")