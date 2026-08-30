student_marks = {}

n = int(input("How many student marks do you want to add? "))

for i in range(n):
    name = input("Enter name: ")
    marks = input("Enter marks in english: ")

    student_marks[name] = marks

print("The marks obtained by student:", student_marks)