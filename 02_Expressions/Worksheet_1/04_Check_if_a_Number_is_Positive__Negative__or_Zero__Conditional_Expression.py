"""
4. Check if a Number is Positive, Negative, or Zero (Conditional Expression)
Use a single line expression to print whether a number is positive, negative, or zero.
Sample Input: num = -8
"""
num=int(input("Enter the num: "))

print("Positive" if(num>0) else "Negative" if(num<0) else "zero" )