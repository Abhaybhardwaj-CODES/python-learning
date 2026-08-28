Str = input("Enter a string: ")
count = 0
for i in range(len(Str)):
    if Str[i] == " ":
        count = count + 1
print("The number of spaces in the string is:", count)