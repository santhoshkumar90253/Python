"""
12. Given a voltage and current reading, print "Power OK" if both are in safe ranges, otherwise print specific error:
- Voltage out of 3.0–3.3V: "Voltage Error"
- Current out of 10–500mA: "Current Error"
- Both out: "Power Error"
"""

voltage = float(input("Enter voltage (in volts): "))
current = int(input("Enter current (in mA): "))
voltage_ok = 3.0 <= voltage <= 3.3
current_ok = 10 <= current <= 500
if voltage_ok and current_ok:
    print("Power OK")
elif not voltage_ok and not current_ok:
    print("Power Error")
elif not voltage_ok:
    print("Voltage Error")
else:
    print("Current Error")