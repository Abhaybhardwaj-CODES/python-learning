class Car:
    def __init__(self,model, color, year, price, brand ,mileage ):

        self.model = model
        self.color = color
        self.year = year
        self.price = price
        self.mileage = mileage
        self.brand = brand
        

    def display(self):
        print("Model:", self.model)
        print("Color:", self.color)
        print("Year:", self.year)
        print("Brand:", self.brand)
        print("Price:", self.price)
        print("Mileage:", self.mileage)