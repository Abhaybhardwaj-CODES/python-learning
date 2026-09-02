def Add_student():
    added_students = []
    print("Enter student details:")
    name = input("Name: ")
    age = int(input("Age: "))
    grades = input("Grade in sub1: ")
    student = {"name": name, "age": age, "grades": grades}
    added_students.append(student)
    print("Student added successfully.")
def view_students():
    if not added_students:
        print("No students found.")
    else:
        print("Student List:")
        for student in added_students:
            print(f"Name: {student['name']}, Age: {student['age']}, Grades: {student['grades']}")

def search_student():
    name = input("Enter student name to search: ")
    for student in added_students:
        if student['name'] == name:
            print(f"Student found: Name: {student['name']}, Age: {student['age']}, Grades: {student['grades']}")
            return
    print("Student not found.")

def update_student():
    name = input("Enter student name to update: ")
    for student in added_students:
        if student['name'] == name:
            new_age = int(input("Enter new age: "))
            new_grades = input("Enter new grades: ")
            student['age'] = new_age
            student['grades'] = new_grades
            print("Student updated successfully.")
            return
    print("Student not found.")


def delete_student():
    name = input("Enter student name to delete: ")
    for student in added_students:
        if student['name'] == name:
            added_students.remove(student)
            print("Student deleted successfully.")
            return
    print("Student not found.")


def calculate_grade():
    name = input("Enter student name to calculate grade: ")
    for student in added_students:
        if student['name'] == name:
            grades = student['grades']
            calculate_grade = sum(int(grade) for grade in grades.split(','))
            print(f"Student {name} has grades of {grades}.")
            return
    print("Student not found.")     

           
def sort_students():
    sorted_students = sorted(added_students, key=lambda x: x['name'])
    print("Sorted Student List:")
    for student in sorted_students:
        print(f"Name: {student['name']}, Age: {student['age']}, Grades: {student['grades']}") 

def validate_student_data():
    name = input("Enter student name to validate: ")
    for student in added_students:
        if student['name'] == name:
            if len(student['name']) < 3:
                print("Student name must be at least 3 characters long.")
            elif student['age'] < 5 or student['age'] > 18:
                print("Student age must be between 5 and 18 .")
            elif not all(grade.isdigit() and 0 <= int(grade) <= 100 for grade in student['grades'].split(',')):
                print("Grades must be numbers between 0 and 100.")
            else:
                print("Student data is valid.")
            return
    print("Student not found.")

def save_data():
    with open("students_data.txt", "w") as file:
        for student in added_students:
            file.write(f"{student['name']},{student['age']},{student['grades']}\n")
    print("Data saved successfully.")

def load_data():
    global added_students
    added_students = []
    try:
        with open("students_data.txt", "r") as file:
            for line in file:
                name, age, grades = line.strip().split(',')
                added_students.append({
                    'name': name,
                    'age': int(age),
                    'grades': grades
                })
        print("Data loaded successfully.")
    except FileNotFoundError:
        print("No existing data found.")

while True:
    print("Welcome to the Student Management System")
    
    print("1. Add Student ")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Calculate Grade")
    print("7. Sort Students")
    print("8. Validate Student Data")
    print("9. Save Data")
    print("10. Load Data")
    print("11. Exit")

    choice = input("Enter your choice (1-11): ")
    print("\n")
    print("Your choice is:", choice)


    if choice == '1':
        Add_student()
    elif choice == '2':
        view_students()
    elif choice == '3': 
        search_student()
    elif choice == '4':
        update_student()
    elif choice == '5':
        delete_student()
    elif choice == '6':
        calculate_grade()
    elif choice == '7':
        sort_students()
    elif choice == '8':
        validate_student_data()
    elif choice == '9':
        save_data()
    elif choice == '10':
        load_data()
    elif choice == '11':
        print("Exiting the Student Management System. Goodbye!")
        break        


