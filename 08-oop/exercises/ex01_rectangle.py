"""
⭐ Exercise 1 – Rectangle

Create a Rectangle class:
  - __init__(self, width, height)
  - area()       → width * height
  - perimeter()  → 2 * (width + height)
  - is_square()  → True if width == height
  - __str__      → "Rectangle(4 x 5)"
"""

# Write your class here 👇


r = Rectangle(4, 5)
assert r.area() == 20
assert r.perimeter() == 18
assert r.is_square() is False
assert Rectangle(3, 3).is_square() is True
assert str(r) == "Rectangle(4 x 5)"
print("✅ All checks passed!")
