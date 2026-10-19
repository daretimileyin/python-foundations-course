"""
⭐ Exercise 2 – BMI Calculator

BMI = weight_kg / (height_m ** 2)

Categories:
    below 18.5      → "Underweight"
    18.5 to < 25    → "Normal"
    25 to < 30      → "Overweight"
    30 and above    → "Obese"

After the checks pass, add a main() that asks the user for their
weight and height and prints their BMI (1 decimal place) and category.
"""


def calculate_bmi(weight_kg, height_m):
    """Return the BMI rounded to 1 decimal place."""
    # TODO
    pass


def bmi_category(bmi):
    """Return the category name for a BMI value."""
    # TODO
    pass


assert calculate_bmi(70, 1.75) == 22.9
assert bmi_category(17.0) == "Underweight"
assert bmi_category(22.9) == "Normal"
assert bmi_category(27.5) == "Overweight"
assert bmi_category(31.0) == "Obese"
print("✅ All checks passed!")
