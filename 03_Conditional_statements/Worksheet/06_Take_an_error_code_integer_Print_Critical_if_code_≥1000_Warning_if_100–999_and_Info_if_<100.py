"""
6. Take an error code (integer). Print "Critical" if code ≥1000, "Warning" if 100–999, and "Info" if <100.
Input: 230
Output: Warning
"""
code = int(input("Enter error code: "))
if code >= 1000:
    print("Critical")
elif (100 <= code <= 999):
    print("Warning")
else:
    print("Info")