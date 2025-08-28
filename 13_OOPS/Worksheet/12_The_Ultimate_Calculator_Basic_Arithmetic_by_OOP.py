'''
12. The Ultimate Calculator: Basic Arithmetic by OOP
Scenario:
Build your own pocket calculator with class-based design.

What you’ll learn:
Encapsulating operations in methods
Using OOP for real utilities

Task:
Log Session a Calculator class with methods for add, subtract, multiply, and divide.

Example:
Adding 4 and 5, then dividing 10 by 2:
'''
class calc:
    def __init__(self,x,y):
        self.x,self.y=x,y

    def add(self):
        return self.x+self.y
    
    def sub(self):
        return self.x-self.y
    
    def mul(self):
        return self.x*self.y
    
    def div(self):
        return self.x//self.y
    
x=calc(5,4)
y=calc(10,2)
print(x.add(),y.div())