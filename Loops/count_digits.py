Digit = int(input("enter the Digit: "))
count = 0
while Digit > 0:
    Digit = Digit // 10
    count += 1
print(f"The number of digits is: {count}")