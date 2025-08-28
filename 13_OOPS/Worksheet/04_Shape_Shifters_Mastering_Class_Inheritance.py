'''
4. Shape Shifters: Mastering Class Inheritance
Scenario:
Imagine you’re building a drawing tool. You have a general Shape, but want to specialize it into Circle and Square.

What you’ll learn:
The basics of inheritance
How subclasses can extend or override parent class functionality

Task:
Log Session a Shape class with a method called draw(). Inherit and customize in Circle and Square.

Example:
If you create a Circle and ask it to draw():
'''
class shape:
    def draw(self):
        print("Drawing Shape")

class circle(shape):
    def draw(self):
       print("Drawing Circle")

class square(shape):
    def draw(self):
        print("Drawing Square")

c=circle()
s=square()
c.draw()
s.draw()