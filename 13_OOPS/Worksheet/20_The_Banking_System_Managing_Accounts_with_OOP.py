'''
20. The Banking System: Managing Accounts with OOP
Scenario:
Simulate a simple bank system: create accounts, deposit, withdraw, and check balances.

What you’ll learn:
Using classes for real-life simulations
Method design and data encapsulation

Task:
Log Session a BankAccount class with methods for deposit, withdraw, and balance check.

Example:
Start with balance 1000, deposit 500, withdraw 300, show balance.
'''

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self._balance = balance  

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
        else:
            print("Insufficient funds or invalid withdrawal")

    def get_balance(self):
        return self._balance

account = BankAccount("Ajith", 1000)
account.deposit(500)
account.withdraw(300)
print(account.get_balance()) 