Str = input("Enter a string: ")

repeating_characters = ""
for i in range(len(Str)):
    if Str[i] in repeating_characters:
        continue
    count = 0
    for j in range(len(Str)):
        if Str[i] == Str[j]:
            count = count + 1
    if count > 1:
        repeating_characters = repeating_characters + Str[i]

print("The repeating characters in the string are:", repeating_characters)