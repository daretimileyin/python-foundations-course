"""Example 02 – Variables and data types."""

name = "Ada Lovelace"
birth_year = 1815
height_m = 1.65
is_programmer = True
middle_name = None

print(name, type(name))
print(birth_year, type(birth_year))
print(height_m, type(height_m))
print(is_programmer, type(is_programmer))
print(middle_name, type(middle_name))

# Variables can be re-assigned
score = 0
print("Score:", score)
score = score + 10
print("Score:", score)
score += 5
print("Score:", score)

# Multiple assignment
x, y, z = 1, 2, 3
print(x, y, z)

# Swapping two variables, Python style
x, y = y, x
print("After swap:", x, y)
