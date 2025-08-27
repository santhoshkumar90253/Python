'''
25. Convert Numeric Words to Actual Numbers
Explanation: Replace words like 'one', 'two' with their numeric equivalents.
Input: "I have one apple and two oranges."
Expected Output: "I have 1 apple and 2 oranges."
'''

def replace(s):
    l=s.split()
    print(l) 
    d = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4','five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9',
                   'ten': '10'}
    res=[]
    for i in l:
        if i in d:
            num=d[i.lower()]
            res.append(num)
        else:
            res.append(i)
    print(res)
    return ' '.join(res)

s=input("Enter the string:")
print("After replacement:",replace(s))