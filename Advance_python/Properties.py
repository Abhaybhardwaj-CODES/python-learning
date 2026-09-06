class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value <= 0:
            raise ValueError("radius must be positive")
        self._radius = value

    @property
    def area(self):              # read-only computed property
        return 3.14159 * self._radius ** 2

c = Circle(5)
print(c.radius)   # 5           <- looks like attribute access
print(c.area)     # 78.53975    <- computed on the fly, no parens needed
c.radius = 10     # goes through the setter, validated
c.radius = -1     # raises ValueError
c.area = 100      # raises AttributeError: no setter defined -> read-only