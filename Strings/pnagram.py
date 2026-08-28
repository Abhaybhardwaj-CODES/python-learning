Str = input("Enter a string: ")
for i in Str: 
    if i.isalpha() == False:
        print("The string is not a pangram.")
        break
    else:
        print("The string is a pangram.")
        break