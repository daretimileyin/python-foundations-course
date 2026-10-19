class NegativeAgeError(Exception):
    pass


class UnrealisticAgeError(Exception):
    pass


def validate_age(age):
    if age < 0:
        raise NegativeAgeError(f"{age} is negative")
    if age > 130:
        raise UnrealisticAgeError(f"{age} is older than anyone has ever lived")
    return age


def main():
    try:
        age = validate_age(int(input("Your age: ")))
    except ValueError:
        print("Please type a whole number.")
    except NegativeAgeError as error:
        print(f"Ages can't be negative ({error}).")
    except UnrealisticAgeError as error:
        print(f"Hmm, really? {error}.")
    else:
        print(f"Thanks! Age {age} recorded.")


if __name__ == "__main__":
    main()
