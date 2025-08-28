'''
15. Stack in Python: Undo That Move!
Scenario:
Log Session a feature like "undo" in a drawing app.

What you’ll learn:
How to build a stack (LIFO) using classes
Using lists for stack operations

Task:
Implement a Stack class with push and pop methods.

Example:
Push 10, then 20; pop an element.
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

stack = Stack()
stack.push(10)
stack.push(20)
print(stack.pop())  