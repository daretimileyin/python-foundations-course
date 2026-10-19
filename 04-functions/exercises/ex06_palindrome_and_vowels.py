"""
⭐⭐⭐ Exercise 6 – Text Functions

Hints: text[::-1] reverses a string; text.lower(); char.isalpha()
"""


def is_palindrome(text):
    """
    Return True if text reads the same forwards and backwards,
    ignoring case, spaces and punctuation.
    """
    # TODO
    pass


def count_vowels(text):
    """Return the number of vowels (a, e, i, o, u) in text, any case."""
    # TODO
    pass


def capitalize_words(text):
    """Return text with the first letter of every word capitalised (no .title()!)."""
    # TODO
    pass


assert is_palindrome("racecar") is True
assert is_palindrome("A man, a plan, a canal: Panama") is True
assert is_palindrome("python") is False
assert count_vowels("Hello World") == 3
assert capitalize_words("hello big world") == "Hello Big World"
print("✅ All checks passed!")
