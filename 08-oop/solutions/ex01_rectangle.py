class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def is_square(self):
        return self.width == self.height

    def __str__(self):
        return f"Rectangle({self.width} x {self.height})"


r = Rectangle(4, 5)
assert r.area() == 20
assert r.perimeter() == 18
assert r.is_square() is False
assert Rectangle(3, 3).is_square() is True
assert str(r) == "Rectangle(4 x 5)"
print("✅ All checks passed!")
