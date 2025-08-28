'''
7. Are You One of Us? Checking Class Membership
Scenario:
You want to make sure a Bus object can access special parking. But only if it’s really a Vehicle.

What you’ll learn:
Using isinstance() to check an object’s class or parent classes
Dynamic type safety

Task:
Check if a Bus object is an instance of Vehicle.

Example:
You check with isinstance() for a Bus object.
'''

class vehicle:
    pass
class bus(vehicle):
    pass

b=bus()
print(isinstance(b,vehicle))