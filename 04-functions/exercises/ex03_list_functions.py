"""
⭐⭐ Exercise 3 – Functions on Lists
"""


def average(numbers):
    """Return the average of a list. Return 0 for an empty list."""
    # TODO
    pass


def count_above(numbers, threshold):
    """Return how many numbers are greater than threshold."""
    # TODO
    pass


def only_positive(numbers):
    """Return a NEW list containing only the positive numbers."""
    # TODO
    pass


assert average([2, 4, 6]) == 4
assert average([]) == 0
assert count_above([1, 5, 10, 15], 5) == 2
assert only_positive([-2, 3, 0, 7, -1]) == [3, 7]
print("✅ All checks passed!")
