import math


class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        raise NotImplementedError("Subclasses must implement area()")

    def describe(self):
        return f"{self.name} with area {self.area():.2f}"


class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2


class Square(Shape):
    def __init__(self, side):
        super().__init__("Square")
        self.side = side

    def area(self):
        return self.side ** 2


class Triangle(Shape):
    def __init__(self, base, height):
        super().__init__("Triangle")
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


shapes = [Circle(5), Square(4), Triangle(6, 3)]
for shape in shapes:
    print(shape.describe())
print("Largest:", max(shapes, key=lambda s: s.area()).name)

assert round(shapes[0].area(), 2) == 78.54
assert shapes[1].area() == 16
assert shapes[2].area() == 9
assert shapes[0].describe() == "Circle with area 78.54"
print("✅ All checks passed!")
