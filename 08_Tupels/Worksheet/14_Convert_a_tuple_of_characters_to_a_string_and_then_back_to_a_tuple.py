'''
Description: Convert a tuple of characters to a string and then back to a tuple.
Useful for text manipulation and transitioning between data representations.
Input: t = ('P', 'y', 't', 'h', 'o', 'n')
Output: String: "Python"
Tuple: ('P', 'y', 't', 'h', 'o', 'n')
'''

t=('s','a','n','t','h', 'o', 's', 'h')
t=''.join(t)
print(t)
t=tuple(t)
print(t)