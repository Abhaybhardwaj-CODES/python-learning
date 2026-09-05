import json
try:
    with open("employees.json", "r") as file:
        employees = json.load(file)
except FileNotFoundError:
    employees = {}

    while True:
        print("\n--- EMPLOYEE DATABASE ---")
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Search Employee")
        print("4. Exit")

        choice = input("Enter your choice: ")

        # Add employee
        if choice == "1":
            emp_id = input("Enter employee ID: ")
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            department = input("Enter department: ")

            employees[emp_id] = {
                "name": name,
                "age": age,
                "department": department
            }

            with open("employees.json", "w") as file:
                json.dump(employees, file, indent=4)

            print("Employee added successfully!")

        # View employees
        elif choice == "2":
            if not employees:
                print("No employees found.")
            else:
                for emp_id, details in employees.items():
                    print("\nEmployee ID:", emp_id)
                    print("Name:", details["name"])
                    print("Age:", details["age"])
                    print("Department:", details["department"])

        # Search employee
        elif choice == "3":
            emp_id = input("Enter employee ID to search: ")

            if emp_id in employees:
                print("\nEmployee Found!")
                print("Name:", employees[emp_id]["name"])
                print("Age:", employees[emp_id]["age"])
                print("Department:", employees[emp_id]["department"])
            else:
                print("Employee not found.")

        # Exit
        elif choice == "4":
            print("Program ended.")
            break