'''
19. Queue It Up: Fair Turn for All
Scenario:
Manage waiting lines—like people in a ticket queue.

What you’ll learn:
Implementing a queue (FIFO) in Python
Real-world queue management

Task:
Build a Queue class with enqueue and dequeue methods.

Example:
Enqueue 10, then 20; dequeue once.
'''

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item) 

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)  
        return "Queue is empty"

    def is_empty(self):
        return len(self.items) == 0

    def display(self):
        print(self.items)

q = Queue()
q.enqueue(10)
q.enqueue(20)
print(q.dequeue()) 