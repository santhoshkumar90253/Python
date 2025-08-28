'''
5. One for All: The Magic of Class Attributes
Scenario:
All students in a school belong to the same institution. How can you ensure this is reflected in every student object?

What you’ll learn:
Class (static) attributes: properties shared by all instances
When and why to use them

Task:
Define a Student class where every student has the same school_name.

Example:
If you create two students and print their school_name:
'''

class student:
    school_name="SSV"
    
    def __init__(self,name):
        self.name=name

    def display(self):
        print(f"{self.name}: {student.school_name}")

s1=student("SANTHOSH")
s2=student("RAM")

s1.display()
s2.display()