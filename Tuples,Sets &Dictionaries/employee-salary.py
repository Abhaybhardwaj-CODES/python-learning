employee_salary = {}

n = int(input("How many contacts do you want to add? "))

for i in range(n):
    name = input("Enter name: ")
    salary = input("Enter salary: ")

    employee_salary[name] = salary

print("The employee salary :", employee_salary)