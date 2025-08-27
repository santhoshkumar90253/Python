"""
14. Accept a device mode value:
- 0: "Standby"
- 1: "Active"
- 2: "Fault"
- Any other: "Unknown mode"
"""

v=int(input("Enter the device mode value:"))
if v==0:
    print("standby")
elif v==1:
    print("Active")
elif v==2:
    print("Fault")
else:
    print("unknown mode")