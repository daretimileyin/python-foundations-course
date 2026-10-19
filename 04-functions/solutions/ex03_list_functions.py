def average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)


def count_above(numbers, threshold):
    return len([n for n in numbers if n > threshold])


def only_positive(numbers):
    return [n for n in numbers if n > 0]


assert average([2, 4, 6]) == 4
assert average([]) == 0
assert count_above([1, 5, 10, 15], 5) == 2
assert only_positive([-2, 3, 0, 7, -1]) == [3, 7]
print("✅ All checks passed!")
