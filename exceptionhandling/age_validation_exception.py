class AgeValidationError(Exception):
    pass


age = int(input("Enter your age: "))

try:
    if age < 18:
        raise AgeValidationError("Age must be 18 or above")
    
    print("Age is valid")

except AgeValidationError as e:
    print("Invalid age:", e)