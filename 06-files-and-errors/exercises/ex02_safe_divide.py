"""
⭐ Exercise 2 – Safe Divide

Write safe_divide(a, b) that:
  - returns a / b normally
  - returns None if b is zero (instead of crashing)
  - returns None if a or b can't be converted to a number,
    e.g. safe_divide("ten", 2)

Use try/except. Don't use `if b == 0`!
"""


def safe_divide(a, b):
    # TODO
    pass


assert safe_divide(10, 2) == 5
assert safe_divide("9", "3") == 3
assert safe_divide(1, 0) is None
assert safe_divide("ten", 2) is None
print("✅ All checks passed!")
