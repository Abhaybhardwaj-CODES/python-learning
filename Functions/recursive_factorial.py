def fact(n):
    """Return the factorial of a given number n."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    elif n == 0 or n == 1:
        return 1
    else:
        return n * fact(n - 1)

n = int(input("Enter a number to calculate its factorial: "))
print(f"The factorial of {n} is {fact(n)}")