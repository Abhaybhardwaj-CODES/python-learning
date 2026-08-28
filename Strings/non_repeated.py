Str = input("Enter a string: ")

non_repeated_characters = ""
for i in range(len(Str)):
    if Str[i] not in non_repeated_characters:
        non_repeated_characters = non_repeated_characters + Str[i]
        

print("The non-repeated characters in the string are:", non_repeated_characters)
