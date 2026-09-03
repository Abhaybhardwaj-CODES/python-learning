class Employee:
    def __init__(self,name, age,emp_id,salary):
        self.name = name
        self.age = age
        self.emp_id = emp_id
        self.salary = salary

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Employee ID:", self.emp_id)
        print("Salary:", self.salary)    