class exception_handling:
    def __init__(self, name, age, roll_no):
        self.name = name
        self.age = age
        self.roll_no = roll_no

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Roll No:", self.roll_no)


exception_handling = exception_handling("John Doe", 20, "12345")

try:
    if exception_handling.age <= 0:
        raise ValueError("Age must be a positive integer.")
    else:
        print("Age is valid.")

    exception_handling.display()

except ValueError as e:
    print("Age Validation Error:", e)

finally:
    print("Execution completed.")