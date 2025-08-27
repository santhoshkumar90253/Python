"""
3. Enter a temperature and print "Overheat" (>75°C), "Normal" (25-75°C), or "Low Temp" (<25°C).
Input: 18
Output: Low Temp
"""

temp=float(input("Enter the temperature value: "))
if temp>75:
    print("overheat")
elif temp<25:
    print("Low temp")
else:
    print("Normal")