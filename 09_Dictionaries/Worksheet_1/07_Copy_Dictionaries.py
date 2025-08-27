'''Copy Dictionaries
Copying dictionaries is critical when you need to manipulate data without affecting the original.
Make a shallow copy of d = {'p': 2, 'q': 3} and print the copy.
Show what happens when you do b = a with a = {'x': [1, 2]} and then modify b['x']. What happens to a?
Log Session a copy of original = {'car': 'red', 'bike': 'blue'}. Change the 'car' in the copy to 'green' and 
print both dictionaries.
Expected Output: Original remains unchanged.
Explain (with code) the difference between a shallow copy and a deep copy using a nested dictionary. 
Show the effect of changing an inner list.'''

import copy  
# Shallow copy using .copy()
d = {'p': 2, 'q': 3}
d_copy = d.copy()
print("Shallow copy of d:", d_copy)

a = {'x': [1, 2]}
b = a  # b refers to the same dictionary as a
b['x'].append(3)
print("\nAfter modifying b['x']:")
print("a =", a)  # a also changes
print("b =", b)

# Changing copy doesn't affect original
original = {'car': 'red', 'bike': 'blue'}
session_copy = original.copy()
session_copy['car'] = 'green'

print("\nOriginal dictionary:", original)
print("Modified copy:", session_copy)

# nested dictionary
nested = {'colors': ['red', 'blue'], 'shapes': ['circle', 'square']}

# Shallow copy
shallow = nested.copy()

# Deep copy
deep = copy.deepcopy(nested)

# Modify the inner list
shallow['colors'].append('green')
deep['shapes'].append('triangle')

print("\nAfter modifying inner lists:")
print("Original:", nested)
print("Shallow Copy:", shallow)
print("Deep Copy:", deep)