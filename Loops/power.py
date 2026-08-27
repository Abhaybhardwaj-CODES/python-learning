base = int(input("Enter the base number: "))
power = int(input("Enter the exponent: "))
result = 1
for i in range(power):
    result *= base
print(f"{base} raised to the power of {power} is {result}")