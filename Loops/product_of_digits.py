digit = int(input("Enter a digit: ")) 
product_of_digits = 1
while digit > 0:
    product_of_digits *= digit % 10
    digit = digit // 10
print(f"Product of the digits is: {product_of_digits}")



for i in range(1, digit + 1):
    product_of_digits *= i
print("Product of the digits is:", product_of_digits)