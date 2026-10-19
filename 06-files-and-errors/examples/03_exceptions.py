"""Example 03 – Handling and raising exceptions."""


def ask_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("  ⚠️ That isn't a number, try again.")


a = ask_number("First number: ")
b = ask_number("Second number: ")

try:
    result = a / b
except ZeroDivisionError:
    print("You can't divide by zero!")
else:
    print(f"{a} / {b} = {result}")
finally:
    print("(calculation finished)")

# Catching and inspecting an error
try:
    with open("this_file_does_not_exist.txt") as f:
        f.read()
except FileNotFoundError as error:
    print(f"\nCaught an error: {error}")


# Raising errors
def set_age(age):
    if not isinstance(age, int):
        raise TypeError("Age must be a whole number")
    if age < 0 or age > 150:
        raise ValueError(f"{age} is not a realistic age")
    return age


for value in [25, -5, "ten"]:
    try:
        print("Age set to", set_age(value))
    except (ValueError, TypeError) as error:
        print(f"Rejected {value!r}: {error}")
