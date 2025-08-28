'''
17. Shopping Cart: OOP for Online Stores
Scenario:
Simulate adding/removing items and computing the bill in an online store.

What you’ll learn:
Real-world application of classes
Encapsulation and methods

Task:
Design a ShoppingCart class with add, remove, and total methods.

Example:
Add "Book" (2 × 200) and "Pen" (5 × 20); show total.
'''


class ShoppingCart:
    def __init__(self):
        self.items = {}  

    def add(self, item, quantity, price):
        if item in self.items:
            old_qty= self.items[item]
            self.items[item] = (old_qty + quantity, price)
        else:
            self.items[item] = (quantity, price)

    def remove(self, item):
        if item in self.items:
            del self.items[item]

    def total(self):
        return sum(qty * price for qty, price in self.items.values())

cart = ShoppingCart()
cart.add("Book", 2, 200)  
cart.add("Pen", 5, 20)   
print(cart.total())       
