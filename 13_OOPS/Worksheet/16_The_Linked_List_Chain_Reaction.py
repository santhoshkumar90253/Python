'''
16. The Linked List: Chain Reaction
Scenario:
Store and process data efficiently, like songs in a playlist.

What you’ll learn:
Building a linked list from scratch
Understanding nodes and pointers

Task:
Write a LinkedList class with insert, delete, and display.

Example:
Add 10, then 20, and display list.
'''


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node  
        else:
            current = self.head
            while current.next:  
                current = current.next
            current.next = new_node  

    def delete(self, data):
        current = self.head
        previous = None
        while current:
            if current.data == data:
                if previous:
                    previous.next = current.next  
                else:
                    self.head = current.next  
                return
            previous = current
            current = current.next

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> " if current.next else "")
            current = current.next
        print()

ll = LinkedList()
ll.insert(10)
ll.insert(20)
ll.display()   