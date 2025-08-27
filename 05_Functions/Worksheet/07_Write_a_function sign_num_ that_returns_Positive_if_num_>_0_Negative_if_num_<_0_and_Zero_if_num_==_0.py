'''Write a function sign(num) that returns 'Positive' if num > 0, 'Negative' if num < 0, and 'Zero' if num == 0'''
def sign(num):
    return 'Zero' if num==0 else 'Positive' if num>0 else 'Negative'
n=int(input("Enter the number: "))
print(f'the given number is {sign(n)}')