'''Python - Check if a given string is binary string or not
 What does set(note) show you?'''
def is_binary_string(s):
    return set(s).issubset({'0', '1'})

s = input("Enter a string: ")

if is_binary_string(s):
    print("Yes, it's a binary string.")
else:
    print("No, it's not a binary string.")