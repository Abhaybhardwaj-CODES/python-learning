password = input("Enter a password: ")
has_uppercase = any(char.isupper() for char in password)
has_lowercase = any(char.islower() for char in password)
has_digit = any(char.isdigit() for char in password)
has_special_char = any(not char.isalnum() for char in password)
if len(password) >= 8 and has_uppercase and has_lowercase and has_digit and has_special_char:
    print("Password is strong.")
elif len(password) < 8:
    print("Password is weak. It should be at least 8 characters long.")
elif not has_uppercase:
    print("Password is weak. It should contain at least one uppercase letter.")
elif not has_lowercase:
    print("Password is weak. It should contain at least one lowercase letter.")
elif not has_digit:
    print("Password is weak. It should contain at least one digit.")
elif not has_special_char:
    print("Password is weak. It should contain at least one special character.")
else:
    print("Password is weak. Please ensure it meets all the criteria.")       
