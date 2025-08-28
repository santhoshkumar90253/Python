'''
9. Polymorphism in the Real World: Area of Shapes
Scenario:
You’re making a geometry tool. Different shapes need to compute area, but each does it differently.

What you’ll learn:
Polymorphism: different classes, same interface
Practical OOP design patterns

Task:
Log Session a Shape base class with an area() method, then implement it differently in Circle and Square.

Example:
If you create a Square with side 4 and call area():
'''

import math
class shape:
    def area():
        print("AREA")
class circle(shape):
    def area(self,r):
        return math.pi*r**2
class square(shape):
    def area(self,s):
        return s*s

c=circle()
print(round(c.area(2),2))
s=square()
print(s.area(2))