num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
code = input("Enter operation (A/S/M/D): ").upper()
if code == "A": result = num1 + num2
elif code == "S": result = num1 - num2
elif code == "M": result = num1 * num2
elif code == "D": result = num1 / num2
print("Result:", result)