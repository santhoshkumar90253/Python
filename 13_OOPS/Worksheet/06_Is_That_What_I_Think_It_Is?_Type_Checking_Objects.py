'''
6. Is That What I Think It Is? Type Checking Objects
Scenario:
You’re building a dynamic form. You need to know if a user input is a string, number, or something else.

What you’ll learn:
How to use type() and why it’s useful
Avoiding type errors in your code

Task:
Check and print the type of various objects.

Example:
You create an integer and a string and check their types.
'''

age = int(input("Enter the age:"))
name = input("enter the name:")
price = float(input("Enter the price:"))


print(type(age))       
print(type(name))      
print(type(price))