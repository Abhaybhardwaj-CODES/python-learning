def validation_func(username, password):
    if len(username) < 5:
        return "Username must be at least 5 characters long."
    if len(password) < 8:
        return "Password must be at least 8 characters long."
    if not any(char.isdigit() for char in password):
        return "Password must contain at least one digit."
    if not any(char.isupper() for char in password):
        return "Password must contain at least one uppercase letter."
    if not any(char.islower() for char in password):
        return "Password must contain at least one lowercase letter."
    if not any(char in "!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~" for char in password):
        return "Password must contain at least one special character."
    return "Validation successful."

username = input("Enter username: ")
password = input("Enter password: ")
if validation_func(username, password) == "Validation successful.":
    print("Username and password are valid.")
else:
    print(validation_func(username, password))