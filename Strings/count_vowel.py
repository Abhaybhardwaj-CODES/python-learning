Str = input("Enter a string: ")
count = 0
for i in range(len(Str)):
    if Str[i] in ["a", "e", "i", "o", "u"]:
        count = count + 1
print("The number of vowels in the string is:", count)