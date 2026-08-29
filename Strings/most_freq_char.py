Str = input("Enter a string: ")

for i in range(len(Str)):
    count = 0
    for j in range(len(Str)):
        if Str[i] == Str[j]:
            count = count + 1
    print("The frequency of", Str[i], "is:", count)
    if count > 1:
        print("The most frequent character is:", Str[i])
        break