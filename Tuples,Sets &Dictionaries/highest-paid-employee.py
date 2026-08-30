employee_salary = {}

n = int(input("How many contacts do you want to add? "))
largest = 0
highest_employee = ""

for i in range(n):
    name = input("Enter name: ")
    salary = int(input("Enter salary: "))

    employee_salary[name] = salary

print("The employee salary :", employee_salary)
for key in employee_salary:
    if employee_salary[key] > largest:
       largest = employee_salary[key]
       highest_employee = key
print(f"highest paid employee:, {largest}")
print(f"Highest paid employee: {highest_employee}")