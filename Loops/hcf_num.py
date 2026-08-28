num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
og_num1 = num1
og_num2 = num2
while num2 != 0:
    num1, num2 = num2, num1 % num2
     
Lcm = (og_num1 * og_num2) // num1
print("The LCM of", og_num1, "and", og_num2, "is:", Lcm)

