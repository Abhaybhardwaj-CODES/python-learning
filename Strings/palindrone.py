Str = input("Enter a string: ")
og_Str = Str
reverse = ""
for i in Str:
    reverse = i + reverse 
if reverse == og_Str:
        print("The string is a palindrome.") 
else:
     print("The string is not a palindrome.")