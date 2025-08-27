'''Generate All Permutations of a String
Explanation: List all possible ways to rearrange the characters.
Input: "abc"
Expected Output: ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']'''
def permute(i, s, res):
    if i == len(s):
        res.append("".join(s))
        return
 
    for j in range(i, len(s)):
        s[i], s[j] = s[j], s[i]
        permute(i + 1, s, res)
        s[i], s[j] = s[j], s[i]
def permutation(s):
    res = []
    permute(0, list(s), res)
    res.sort()
    return res
n=input("Enter the string:")
r=permutation(n)
print(r)