'''Concatenated string with uncommon characters in Python
What does set(s1) ^ set(s2) do?'''
def uncommon_characters(s1, s2):
    uncommon = set(s1) ^ set(s2)
    return ''.join(uncommon)


s1 = input("Enter a string: ")
s2 = input("Enter a string: ")

result = uncommon_characters(s1, s2)
print("Uncommon characters:", result)