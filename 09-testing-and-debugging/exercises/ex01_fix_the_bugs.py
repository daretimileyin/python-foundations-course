"""
⭐ Exercise 1 – Fix the Bugs

There are 4 bugs below. Use the VS Code debugger (breakpoints + F10)
to find them. Fix each one and write a comment explaining what was wrong.

When all bugs are fixed, the asserts at the bottom pass.
"""


def count_vowels(text):
    count = 0
    for char in text:
        if char in "aeiou":
            count += 1
    return count


def reverse_words(sentence):
    words = sentence.split()
    return " ".join(words.reverse())


def grade(score):
    if score > 90:
        return "A"
    elif score > 80:
        return "B"
    else:
        return "C"


def sum_list(numbers):
    total = 0
    for i in range(1, len(numbers)):
        total += numbers[i]
    return total


assert count_vowels("HELLO world") == 3
assert reverse_words("one two three") == "three two one"
assert grade(90) == "A"
assert grade(80) == "B"
assert sum_list([1, 2, 3]) == 6
print("✅ All bugs fixed!")
