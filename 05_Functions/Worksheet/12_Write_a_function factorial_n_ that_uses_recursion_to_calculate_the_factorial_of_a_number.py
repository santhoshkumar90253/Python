'''Write a function factorial(n) that uses recursion to calculate the factorial of a number'''

def factorial(n):
    if(n==0):
        return 1
    return n*factorial(n-1)
n=int(input("Enter the number: "))
print(f"The factorial of {n} is {factorial(n)}")