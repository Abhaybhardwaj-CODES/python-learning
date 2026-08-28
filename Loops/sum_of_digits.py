digit = int(input("Enter a digit: "))
product_of_digits = 1
for i in range(1 ,digit + 1):
    product_of_digits *= i
print("Product of the digits is:", product_of_digits)