class Positive:
    """A descriptor that only allows positive values."""
    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if value <= 0:
            raise ValueError(f"{self.name} must be positive")
        setattr(instance, self.name, value)

class Product:
    price = Positive()     # descriptor instance as a class attribute

    def __init__(self, price):
        self.price = price   # goes through Positive.__set__

p = Product(10)
print(p.price)     # 10 -> goes through Positive.__get__
p.price = -5        # raises ValueError!