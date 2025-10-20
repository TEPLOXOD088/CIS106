# Problem 2: Perform operation based on code

def calculate(num1, num2, op_code):
    if op_code == "A":
        result = num1 + num2
    elif op_code == "S":
        result = num1 - num2
    elif op_code == "M":
        result = num1 * num2
    elif op_code == "D":
        if num2 == 0:
            result = -999
            print("Error: Attempt to divide by zero!")
        else:
            result = num1 / num2
    else:
        print("Invalid operation code.")
        return
    print(f"Number 1: {num1}")
    print(f"Number 2: {num2}")
    print(f"Operation code: {op_code}")
    print(f"Result: {result}")

# Example call
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
op_code = input("Enter operation code (A, S, M, D): ").upper()
calculate(num1, num2, op_code)
