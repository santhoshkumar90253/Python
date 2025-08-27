"""
10. Given three sensor readings, print "Majority High" if at least two readings are above a threshold (e.g., 50), otherwise "Majority Low".
Input: 40, 65, 70
Output: Majority High
"""
s1=int(input("Enter the sensor 1 reading:"))
s2=int(input("Enter the sensor 2 reading:"))
s3=int(input("Enter the sensor 3 reading:"))
if(s1>50 and s2>50) or(s2>50 and s3 >50) or (s1>50 and s3>50):
    print("Majority High")
else:
    print("Majority Low")