a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
operation = input("Enter the operation (+, -, *, /): ")

if operation == "+":
    result = a + b
    print(f"The result of {a} + {b} is: {result}")
elif operation == "-":
    result = a - b
    print(f"The result of {a} - {b} is: {result}")
elif operation == "*":
    result = a * b
    print(f"The result of {a} * {b} is: {result}")
elif operation == "/":
    if b != 0:
        result = a / b
        print(f"The result of {a} / {b} is: {result}")
    else:
        print("Error: Division by zero is not allowed.")