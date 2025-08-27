'''Check If a String is a Binary String
Explanation: Test if the string contains only '0' and '1'.
Input: "101101"
Expected Output: Is binary string: Yes'''
def check_bin(s):
    if set(s).issubset({'0','1'}):
        return True
    return False
s=input("Enter the binary string: ")
print("Is binary string:",'Yes'if check_bin(s) else 'No')