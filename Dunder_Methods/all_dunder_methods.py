class ShoppingBag:

    def __init__(self, items):
        self.items = items

    def __str__(self):
        return f"ShoppingBag: {self.items}"

    def __repr__(self):
        return f"ShoppingBag({self.items})"

    def __len__(self):
        return len(self.items)

    def __getitem__(self, index):
        return self.items[index]

    def __setitem__(self, index, value):
        self.items[index] = value

    def __eq__(self, other):
        return self.items == other.items

    def __lt__(self, other):
        return len(self.items) < len(other.items)

    def __add__(self, other):
        return ShoppingBag(self.items + other.items)

    def __sub__(self, other):
        new_items = self.items.copy()

        for item in other.items:
            if item in new_items:
                new_items.remove(item)

        return ShoppingBag(new_items)

    def __mul__(self, number):
        return ShoppingBag(self.items * number)

    def __contains__(self, item):
        return item in self.items