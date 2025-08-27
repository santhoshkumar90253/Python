"""
4. Given two pin logic levels (0 or 1), print the type of logic gate output if these were inputs to an AND, OR, and XOR gate.
Input: 1, 0
Output: AND: 0, OR: 1, XOR: 1
"""

pin1=int(input("Enter the logic level of pin1:"))
pin2=int(input("Enter the logic level of pin2:"))
print("AND: ", pin1 and pin2,"OR: ",pin1 or pin2,"XOR: ",pin1^pin2)