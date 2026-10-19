import math


def circle_area(radius):
    return math.pi * radius ** 2


def rectangle_area(width, height):
    return width * height


if __name__ == "__main__":
    # Only runs with: python3 geometry.py   (not when imported)
    print("Testing geometry:", circle_area(1), rectangle_area(2, 3))
