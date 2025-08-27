'''
24. Generate All Valid IP Addresses from a String
Explanation: Given a string of digits, form all possible valid IP addresses.
Input: "25525511135"
Expected Output: ['255.255.11.135', '255.255.111.35']
'''

def isValid(s):
    n = len(s)
    if n == 1:
        return True
    val = int(s)
    if s[0] == '0' or val > 255:
        return False
    return True

def generateIpRec(s, index, curr, cnt, res):
    temp = ""
    if index >= len(s):
        return
    if cnt == 3:
        temp = s[index:]
        if len(temp) <= 3 and isValid(temp):
            res.append(curr + temp)
        return
    for i in range(index, min(index + 3, len(s))):
        temp += s[i]
        if isValid(temp):
            generateIpRec(s, i + 1, curr + temp + ".", cnt + 1, res)

def generateIp(s):
    res = []
    generateIpRec(s, 0, "", 0, res)
    return res


s = input("Enter the string:")
res = generateIp(s)
for ip in res:
    print(ip)