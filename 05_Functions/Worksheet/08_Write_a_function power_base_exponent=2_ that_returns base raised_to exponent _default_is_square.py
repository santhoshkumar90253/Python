''' Write a function power(base, exponent=2) that returns base raised to exponent (default is square).'''

def power(base,exponent=2):
    return  base**exponent
n=int(input("Enter the number: "))
y=input("Do you want to enter the exponent yes/no:")

if y=='yes':
    n1=int(input("Enter the exponent:"))
    print(f'The result is {power(n,n1)}')
else:
      print(f'The result is {power(n)}')