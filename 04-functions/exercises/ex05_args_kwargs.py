"""
⭐⭐ Exercise 5 – *args and **kwargs
"""


def multiply_all(*numbers):
    """Return all the numbers multiplied together. With no numbers, return 1."""
    # TODO
    pass


def make_sentence(*words, ending="."):
    """Join the words with spaces, capitalise the first letter, and add the ending."""
    # TODO
    pass


def describe_pet(name, **details):
    """
    Return a description like:
        "Rex: species=dog, age=3"
    (details in the order they were given)
    """
    # TODO
    pass


assert multiply_all(2, 3, 4) == 24
assert multiply_all() == 1
assert make_sentence("python", "is", "fun") == "Python is fun."
assert make_sentence("are", "you", "ready", ending="?") == "Are you ready?"
assert describe_pet("Rex", species="dog", age=3) == "Rex: species=dog, age=3"
print("✅ All checks passed!")
