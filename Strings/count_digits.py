Str = input("Enter a string: ")
count = 0
for i in range(len(Str)):
    if Str[i].isdigit():
        count = count + 1
print("The number of digits in the string is:", count)