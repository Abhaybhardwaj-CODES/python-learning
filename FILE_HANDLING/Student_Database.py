import json

# Load existing data
try:
    with open("students.json", "r") as file:
        students = json.load(file)
except FileNotFoundError:
    students = {}

while True:
    print("\n--- STUDENT DATABASE ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Exit")

    choice = input("Enter your choice: ")

    # Add student
    if choice == "1":
        roll_no = input("Enter roll number: ")
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        course = input("Enter course: ")

        students[roll_no] = {
            "name": name,
            "age": age,
            "course": course
        }

        with open("students.json", "w") as file:
            json.dump(students, file, indent=4)

        print("Student added successfully!")

    # View students
    elif choice == "2":
        if not students:
            print("No students found.")
        else:
            for roll_no, details in students.items():
                print("\nRoll No:", roll_no)
                print("Name:", details["name"])
                print("Age:", details["age"])
                print("Course:", details["course"])

    # Search student
    elif choice == "3":
        roll_no = input("Enter roll number to search: ")

        if roll_no in students:
            print("\nStudent Found!")
            print("Name:", students[roll_no]["name"])
            print("Age:", students[roll_no]["age"])
            print("Course:", students[roll_no]["course"])
        else:
            print("Student not found.")

    # Exit
    elif choice == "4":
        print("Program ended.")
        break

    else:
        print("Invalid choice!")