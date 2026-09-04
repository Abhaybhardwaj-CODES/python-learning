while True:
    try:
        num1 = float(input("Enter first number: "))
        operator = input("Enter operator (+, -, *, /): ")
        num2 = float(input("Enter second number: "))

        if operator == "+":
            result = num1 + num2

        elif operator == "-":
            result = num1 - num2

        elif operator == "*":
            result = num1 * num2

        elif operator == "/":
            if num2 == 0:
                raise ZeroDivisionError("Cannot divide by zero.")
            result = num1 / num2

        else:
            raise ValueError("Invalid operator.")

        print("Result:", result)

    except ValueError as e:
        print("Input Error:", e)

    except ZeroDivisionError as e:
        print("Math Error:", e)

    except Exception as e:
        print("Unexpected Error:", e)

    finally:
        print("Calculation completed.\n")

    choice = input("Do you want to calculate again? (yes/no): ")

    if choice.lower() != "yes":
        print("Calculator closed.")
        break