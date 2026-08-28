Digit = int(input("Enter a number: "))
factorial = 1
sum = 0
while Digit > 0:
    digit = Digit % 10

 
    Digit = Digit // 10
for i in range(1, Digit + 1):
    factorial *= i
    sum = sum + factorial
if sum == Digit:
     print("The number is a strong number")
else:
     print("The number is not a strong number")    



