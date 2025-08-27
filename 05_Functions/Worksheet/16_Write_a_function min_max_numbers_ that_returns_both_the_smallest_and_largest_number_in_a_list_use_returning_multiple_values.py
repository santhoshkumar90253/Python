'''Write a function min_max(numbers) that returns both the smallest and largest number in a list (use returning multiple values).
'''
def min_max(l):
    min=l[0]
    max=l[0]
    for i in l:
        if i>max:
            max=i
        if i<min:
            min=i
    return min,max
n = input("Enter numbers separated by spaces: ")
l = list(map(int, n.split()))
print("List:", l)
min,max=min_max(l)
print(f"The minimum and  maximum in list is {min},{max}")