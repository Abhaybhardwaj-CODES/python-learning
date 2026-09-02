import utilits

def sum(args):
    """Return the sum of the given arguments."""
    total = 0
    for num in args:
        total += num
    return total
def sub(args):
    """Return the subtraction of the given arguments."""
    total = args[0]
    for num in args[1:]:
        total -= num
    return total


def mul(args):
    """Return the multiplication of the given arguments."""
    total = 1
    for num in args:
        total *= num
    return total

def div(args):
    """Return the division of the given arguments."""
    total = args[0]
    for num in args[1:]:
        total /= num
    return total

while True:
    print("select operation -\n" \
          "1. Add\n" \
          "2. Subtract\n" \
          "3. Multiply\n" \
          "4. Divide\n" \
          "5. Exit")

    choice = input("Enter choice(1/2/3/4/5): ")

    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        args = [num1, num2]

        if choice == '1':
            print(num1, "+", num2, "=", sum(args))

        elif choice == '2':
            print(num1, "-", num2, "=", sub(args))

        elif choice == '3':
            print(num1, "*", num2, "=", mul(args))

        elif choice == '4':
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
            else:
                print(num1, "/", num2, "=", div(args))