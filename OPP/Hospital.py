class Hospital:
    def __init__(self, name, location, capacity):
        self.name = name
        self.location = location
        self.capacity = capacity
        self.specialties = []

    def add_specialty(self, specialty):
        self.specialties.append(specialty)    
        if specialty not in self.specialties:
            self.specialties.append(specialty) 
        else:
            print(f"{specialty} is already listed as a specialty.") 

    def display(self):
        print("Hospital Name:", self.name)
        print("Location:", self.location)
        print("Capacity:", self.capacity)
        print("Specialties:", ", ".join(self.specialties))