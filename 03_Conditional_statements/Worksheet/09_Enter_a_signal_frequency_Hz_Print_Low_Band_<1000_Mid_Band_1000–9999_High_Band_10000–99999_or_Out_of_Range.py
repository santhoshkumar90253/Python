"""
9. Enter a signal frequency (Hz). Print "Low Band" (<1000), "Mid Band" (1000–9999), "High Band" (10000–99999), or "Out of Range".
Input: 8000
Output: Mid Band
"""

h = int(input("Enter a signal frequency(HZ): "))
if h<1000:
    print("Low band")
elif (1000 <= h <= 9999):
    print("Mid band")
elif 10000 <= h <= 99999:
    print("High band")
else:
    print("Out of Range")