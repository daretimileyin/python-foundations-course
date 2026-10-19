"""Example 02 – Different kinds of arguments."""


def make_coffee(size="medium", sugar=0, milk=True):
    milk_text = "with milk" if milk else "black"
    return f"A {size} coffee, {milk_text}, {sugar} sugar(s)"


print(make_coffee())
print(make_coffee("large"))
print(make_coffee(sugar=2))
print(make_coffee(milk=False, size="small"))


def average(*numbers):
    """Accept any number of numbers and return their average."""
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)


print("\naverage(1, 2, 3) =", average(1, 2, 3))
print("average(10, 20, 30, 40, 50) =", average(10, 20, 30, 40, 50))


def build_profile(name, **details):
    profile = {"name": name}
    profile.update(details)
    return profile


print("\n", build_profile("Ada", job="Mathematician", born=1815))

# Unpacking a list into arguments
values = [4, 8, 15]
print("average(*values) =", average(*values))
