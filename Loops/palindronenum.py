Num = int(input("Enter a number: "))
original_num = Num
reversed_num = 0
while Num > 0:
    digit = Num % 10
    reversed_num = (reversed_num * 10) + digit
    Num = Num // 10

if original_num == reversed_num:
    print(f"{original_num} is a palindrome.")
else:
    print(f"{original_num} is not a palindrome.")