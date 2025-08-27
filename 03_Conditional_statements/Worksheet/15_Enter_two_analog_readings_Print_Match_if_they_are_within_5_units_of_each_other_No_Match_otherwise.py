"""
15. Enter two analog readings. Print "Match" if they are within 5 units of each other, "No Match" otherwise.
Input: 98, 101
Output: Match
"""

a1=int(input("Enter the analog reading 1:"))
a2=int(input("Enter the analog reading 2:"))
if abs(a1-a2)>=0 and abs(a1-a2)<=5:
    print("Match")
else:
    print("No match")