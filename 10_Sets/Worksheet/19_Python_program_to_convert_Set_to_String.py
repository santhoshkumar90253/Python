'''Python program to convert Set to String
Set has no order—how can you make it alphabetical?'''
import ast
s1 = input("Enter the set:")
s1=ast.literal_eval(s1)
result = ''.join(sorted(s1))
print(result) 
s=''
for i in s1:
    s+=i
print("the string:",s)