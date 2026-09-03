class Restro:
    def __init__(self, name, location, cuisine):
        self.name = name
        self.location = location
        self.cuisine = cuisine
    
    def display(self):
        print("Restaurant Name:", self.name)
        print("Location:", self.location)
        print("Cuisine:", self.cuisine)