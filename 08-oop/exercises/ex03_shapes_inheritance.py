"""
⭐⭐ Exercise 3 – Shapes and Inheritance

1. Create a base class Shape with:
     - __init__(self, name)
     - area()       → raise NotImplementedError
     - describe()   → "Circle with area 78.54"   (area to 2 decimal places)
2. Create child classes that override area():
     - Circle(radius)
     - Square(side)
     - Triangle(base, height)
   Each must call super().__init__ with its name.
3. Put one of each in a list and print describe() for each.
4. Print the shape with the largest area.
"""
import math

# Write your classes here 👇


shapes = [Circle(5), Square(4), Triangle(6, 3)]
assert round(shapes[0].area(), 2) == 78.54
assert shapes[1].area() == 16
assert shapes[2].area() == 9
assert shapes[0].describe() == "Circle with area 78.54"
print("✅ All checks passed!")
