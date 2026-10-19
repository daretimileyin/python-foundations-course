def square(n):
    return n * n


def is_even(n):
    return n % 2 == 0


def full_name(first, last):
    return f"{first} {last}"


assert square(4) == 16
assert square(-3) == 9
assert is_even(10) is True
assert is_even(7) is False
assert full_name("Ada", "Lovelace") == "Ada Lovelace"
print("✅ All checks passed!")
