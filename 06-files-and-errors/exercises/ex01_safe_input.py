"""
⭐ Exercise 1 – Safe Input

Write two functions that keep asking until the user types a valid value:

    ask_int("Age: ")       → returns an int
    ask_float("Price: ")   → returns a float

Bonus: add optional min_value and max_value parameters to ask_int and
keep asking if the number is out of range.

Test it by typing letters, decimals, empty input, etc.
"""


def ask_int(prompt):
    # TODO
    pass


def ask_float(prompt):
    # TODO
    pass


if __name__ == "__main__":
    age = ask_int("Age: ")
    price = ask_float("Price: ")
    print(f"Got age={age} and price={price}")
