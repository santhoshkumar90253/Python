'''
10. All About Circles: Area and Perimeter
Scenario:
Designing a map app? You’ll want to know the area covered by a circular pond!

What you’ll learn:
Implementing methods with calculations
Understanding encapsulation

Task:
Build a Circle class with area() and perimeter() methods.

Example:
For a circle of radius 3:
'''
import math
class circle:
    def __init__(self,r):
        self.r=r
    def area(self):
        return math.pi*self.r**2
    def perimeter(self):
        return 2*math.pi*self.r

x=circle(2)
print(x.area(),x.perimeter())