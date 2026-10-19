"""
⭐⭐ Exercise 2 – the code to test.

These functions are (probably!) correct. Your job is to write tests for
them in test_text_utils.py. Don't change this file, unless your tests
find a bug. 😉
"""


def word_count(text):
    """Return the number of words in text."""
    return len(text.split())


def is_palindrome(text):
    """True if text reads the same backwards (ignoring case, spaces, punctuation)."""
    cleaned = "".join(c.lower() for c in text if c.isalnum())
    return cleaned == cleaned[::-1]


def truncate(text, max_length):
    """Shorten text to max_length characters, ending with '...' if it was cut.

    Raises ValueError if max_length < 3.
    """
    if max_length < 3:
        raise ValueError("max_length must be at least 3")
    if len(text) <= max_length:
        return text
    return text[: max_length - 3] + "..."


def most_common_letter(text):
    """Return the most common letter (lowercase). Ties → alphabetically first. None if no letters."""
    counts = {}
    for c in text.lower():
        if c.isalpha():
            counts[c] = counts.get(c, 0) + 1
    if not counts:
        return None
    return min(counts, key=lambda letter: (-counts[letter], letter))
