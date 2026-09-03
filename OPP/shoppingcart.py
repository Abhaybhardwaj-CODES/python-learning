class Shoppingcart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
        else:
            print(f"{item} not found in the shopping cart.")

    def display_cart(self):
        if not self.items:
            print("Shopping cart is empty.")
        else:
            print("Items in the shopping cart:")
            for item in self.items:
                print("-", item)