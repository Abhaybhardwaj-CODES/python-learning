class login_exception(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
username = input("Enter your username: ")
password = input("Enter your password: ")
try:
    if username != "admin" or password != "password":
        raise login_exception("Invalid username or password.")
    else:
        print("Login successful!")
except login_exception as e:
    print("Login failed:", e)        