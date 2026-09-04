user_input = input("Enter a some text: ")

try:
    if not user_input:
        raise ValueError("Input cannot be empty.")
    print("You entered:", user_input)
except ValueError as e:
    print("Error:", e)
except Exception as e:
    print("An unexpected error occurred:", e)