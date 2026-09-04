a = int(input("Enter the numerator: "))
b = int(input("Enter the denominator: "))



try:
    numerator = a
    denominator =b
    result = numerator / denominator
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Denominator cannot be zero.")