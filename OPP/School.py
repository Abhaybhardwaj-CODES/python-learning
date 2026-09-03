class School:
    def __init__(self, name, location, num_students ,num_teachers , tillwhichgrade):
        self.name = name
        self.location = location
        self.num_students = num_students
        self.num_teachers = num_teachers
        self.tillwhichgrade = tillwhichgrade
    def display(self):
        print("School Name:", self.name)
        print("Location:", self.location)
        print("Number of Students:", self.num_students)
        print("Number of Teachers:", self.num_teachers)
        print("Till which grade:", self.tillwhichgrade)    