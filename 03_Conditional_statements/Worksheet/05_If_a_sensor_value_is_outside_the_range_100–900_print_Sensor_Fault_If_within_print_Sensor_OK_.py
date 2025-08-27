"""
5. If a sensor value is outside the range 100–900, print "Sensor Fault". If within, print "Sensor OK".
Input: 950
Output: Sensor Fault
"""

sensor_value=float(input("Enter the sensor value: "))
if (sensor_value>=100) and (sensor_value<=900):
    print("Sensor Ok")
else:
    print("Sensor Fault")