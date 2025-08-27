'''Check if a String Contains Special Characters
Explanation: Check if the string contains characters other than letters or numbers.
Input: "Hello@123"
Expected Output: Contains special character: Yes'''
def check_spl(s):
    for i in s:
        if not(i.isalpha() or i.isdigit() or i==' '):
            return True
    return False
s=input("Enter the string: ")
print("Contain special character:",'yes' if check_spl(s) else 'no' )