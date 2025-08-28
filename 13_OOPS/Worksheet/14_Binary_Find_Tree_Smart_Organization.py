'''
14. Binary Find Tree: Smart Organization
Scenario:
Organize data for fast searching, like contacts or scores.

What you’ll learn:
Implementing data structures as classes
Recursion in OOP

Task:
Build a BST class with methods for insertion and search.

Example:
Insert numbers and search for 5.
'''


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        def insert1(current, value):
            if current is None:
                return Node(value)
            if value < current.value:
                current.left = insert1(current.left, value)
            elif value > current.value:
                current.right = insert1(current.right, value)
            return current

        self.root = insert1(self.root, value)

    def search(self, value):
        def search1(current, value):
            if current is None:
                return False
            if current.value == value:
                return True
            elif value < current.value:
                return search1(current.left, value)
            else:
                return search1(current.right, value)

        return search1(self.root, value)

bst = BinarySearchTree()
for num in [8, 3, 10, 1, 6, 14, 4, 7]:
    bst.insert(num)

print('5 is present?',bst.search(5))  
print('6 is present?',bst.search(6))  