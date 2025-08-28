'''
18. Enhanced Stack: Show Me What’s Inside
Scenario:
See the current state of the stack—great for debugging.

What you’ll learn:
Extending existing classes
Useful methods for state visibility

Task:
Add a display method to your Stack class to show its elements.

Example:
Push 1, then 2; display stack.
'''

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)  

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return "Stack is empty"

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return "Stack is empty"

    def display(self):
        print(self.items)  

stack = Stack()
stack.push(1)
stack.push(2)
stack.display()  