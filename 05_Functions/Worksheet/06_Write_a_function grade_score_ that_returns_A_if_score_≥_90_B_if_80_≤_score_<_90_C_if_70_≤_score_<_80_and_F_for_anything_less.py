'''Write a function grade(score) that returns 'A' if score ≥ 90, 'B' if 80 ≤ score < 90, 'C' if 70 ≤ score < 80, 
and 'F' for anything less.'''

def grade(score):
    if score>=90:
        res='A'
    elif 80<=score<90:
        res='B'
    elif 70<=score<80:
        res='C'
    else:
        res='F'
    return res
n=int(input("Enter the score: "))
print(grade(n))