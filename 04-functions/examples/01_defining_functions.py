"""Example 01 – Defining and calling functions."""


def say_hello():
    print("Hello! 👋")


def greet(name):
    print(f"Hello, {name}!")


def add(a, b):
    return a + b


def describe_number(n):
    """Return a short description of a number."""
    if n > 0:
        return "positive"
    if n < 0:
        return "negative"
    return "zero"


def rectangle(width, height):
    """Return the area and perimeter of a rectangle."""
    area = width * height
    perimeter = 2 * (width + height)
    return area, perimeter


say_hello()
greet("Ada")
greet("Alan")

total = add(3, 4)
print("3 + 4 =", total)
print("Using a result in another calculation:", add(10, 20) * 2)

for n in [5, -2, 0]:
    print(n, "is", describe_number(n))

area, perimeter = rectangle(4, 3)
print(f"Area={area}, Perimeter={perimeter}")

# print vs return
value = greet("Grace")     # greet prints, but returns None
print("greet returned:", value)
