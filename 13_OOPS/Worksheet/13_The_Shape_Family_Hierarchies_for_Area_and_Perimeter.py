'''
13. The Shape Family: Hierarchies for Area and Perimeter
Scenario:
Simulate a graphics editor: various shapes with their own formulas.

What you’ll learn:
Creating class hierarchies
Overriding methods for specialized behavior

Task:
Write a Shape base class, then subclasses for Circle, Triangle, and Square, each with its own area/perimeter.

Example:
If you create a Triangle with base 6 and height 4 and call area():
'''


import math

class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement area method")

    def perimeter(self):
        raise NotImplementedError("Subclasses must implement perimeter method")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return round(math.pi * self.radius ** 2, 2)

    def perimeter(self):
        return round(2 * math.pi * self.radius, 2)

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

    def perimeter(self):
        return 4 * self.side

class Triangle(Shape):
    def __init__(self, base, height, side1, side2, side3):
        self.base = base
        self.height = height
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def area(self):
        return 0.5 * self.base * self.height

    def perimeter(self):
        return self.side1 + self.side2 + self.side3

t = Triangle(base=6, height=4, side1=5, side2=5, side3=6)
print(t.area())       
print(t.perimeter())  