def ask_int(prompt, min_value=None, max_value=None):
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("Please enter a whole number.")
            continue
        if min_value is not None and value < min_value:
            print(f"Must be at least {min_value}.")
        elif max_value is not None and value > max_value:
            print(f"Must be at most {max_value}.")
        else:
            return value


def ask_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a number.")


if __name__ == "__main__":
    age = ask_int("Age: ", min_value=0, max_value=130)
    price = ask_float("Price: ")
    print(f"Got age={age} and price={price}")
