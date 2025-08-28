'''
2. The Mysterious Empty Class: Why Bother?
Scenario:
You're designing a game and want to reserve a class for future magical creatures—but for now, it's empty.

What you’ll learn:
Why and how to define an empty class
Using pass and setting up blueprints for future code

Task:
Log Session an empty MagicCreature class and show that you can still make objects from it.

Example:
You make a new MagicCreature object and print its type.
'''

class cricket:
    def __init__(self):
        pass

d=cricket()
print(type(d))