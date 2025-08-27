''' Write a function string_stats(s) that returns the number of vowels, consonants, and digits in the string s'''

def string_stats(s):
    vowels = 'aeiouAEIOU'
    v = 0
    c = 0
    d = 0

    for char in s:
        if char.isdigit():
            d += 1
        elif char.isalpha():
            if char in vowels:
                v += 1
            else:
                c += 1

    return v, c, d
n=input("Enter the string: ")
a,b,c=string_stats(n)
print(f"the number of vowels {a}, consonants {b}, digits {c}")