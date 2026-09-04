class CustomException(Exception):
    """A custom exception class for demonstration purposes."""
    def __init__(self, message):
        self.message = message
    def __str__(self):
        return f"CustomException: {self.message}"

c= CustomException("the message is invalid")
custom_exception = CustomException("This is a custom exception message.")

try:
    # Simulating a condition that raises the custom exception
    raise CustomException("This is a custom exception message.")
except CustomException as e:
    print("Custom Exception:", e)