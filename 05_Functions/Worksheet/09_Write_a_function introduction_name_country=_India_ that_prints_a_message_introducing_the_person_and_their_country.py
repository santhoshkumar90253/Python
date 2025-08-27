''' Write a function introduction(name, country='India') that prints a message introducing the person and their country.'''
def introduction(name,country='India'):
    print(f'"Hi I am {name} and I am coming from {country}"')

n=input("Enter the name of person: ")
y=input("Does the person belong to any other country than India yes/no:")
if y=='yes':
    n1=input("Enter the country name of person:")
    introduction(n,n1)
else:
    introduction(n)