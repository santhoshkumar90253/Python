''' Access Dictionaries
Knowing how to access values by key lets you use and process dictionary data effectively.
Given marks = {'math': 75, 'science': 80}, access and print the marks for 'science'.
What happens if you try to access a key that doesn’t exist in a dictionary? Try to print the value for key 'english' in 
marks = {'math': 75}.
Expected Output: A KeyError.
How can you safely access a value for key 'history' in a dictionary scores without causing an error?
Sample Input: scores = {'math': 80, 'science': 90}
Expected Output: If not present, print a custom message like 'Not found'.
Print all subjects and marks from this dictionary: student = {'math': 90, 'english': 88, 'science': 92}.
Sample Output:
math 90
english 88
science 92'''

marks = {'math': 75, 'science': 80}
print("marks for science:",marks['science'])
#print("marks for science:",marks['english'])         #KeyError
if 'history' in marks.keys():
    print(marks['history'])
else:
    print("Not found")
student = {'math': 90, 'english': 88, 'science': 92}
for i,j in student.items():
    print(i,' = ',j)