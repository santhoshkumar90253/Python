'''
19. Convert Integer to String and Vice Versa
Explanation: Change a number to a string, and a string of digits to an integer.
Input: Integer = 123, String = "456"
Expected Output:
Integer to string: '123'
String to integer: 456
'''
i=input("Enter the string: ")
i=int(i)
print(i,type(i))
i=str(i)
print(i,type(i))