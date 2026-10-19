def calculate_bmi(weight_kg, height_m):
    return round(weight_kg / height_m ** 2, 1)


def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    if bmi < 25:
        return "Normal"
    if bmi < 30:
        return "Overweight"
    return "Obese"


assert calculate_bmi(70, 1.75) == 22.9
assert bmi_category(17.0) == "Underweight"
assert bmi_category(22.9) == "Normal"
assert bmi_category(27.5) == "Overweight"
assert bmi_category(31.0) == "Obese"
print("✅ All checks passed!")


def main():
    weight = float(input("Weight (kg): "))
    height = float(input("Height (m): "))
    bmi = calculate_bmi(weight, height)
    print(f"Your BMI is {bmi} ({bmi_category(bmi)})")


if __name__ == "__main__":
    main()
