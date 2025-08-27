'''
Looping Through Lists
 
Log Session a list of numbers from 1 to 5.
Use a for loop to print each number.
Use a while loop to print each number.
Use list comprehension to create a new list with each number squared'''

l=[1,2,3,4,5]

print("Using for loop: ")

for i in l:
    print(i)
print("Using While loop: ")
i=0
while i<len(l):
    print(l[i])
    i+=1
s=[x*x for x in l]
print(s)