"""
⭐⭐⭐ Exercise 5 – Acronyms and Slugs

1. make_acronym("portable network graphics") → "PNG"
   Ignore the small words "of", "and", "the":
   make_acronym("Bank of America") → "BA"

2. slugify turns a title into a URL-friendly slug:
   - lowercase
   - remove anything that is not a letter, digit or space
   - replace spaces with hyphens; no double hyphens or hyphens at the ends
   slugify("  Hello, World! Python 101  ") → "hello-world-python-101"
"""


def make_acronym(phrase):
    # TODO
    pass


def slugify(title):
    # TODO
    pass


assert make_acronym("portable network graphics") == "PNG"
assert make_acronym("Bank of America") == "BA"
assert make_acronym("the lord of the rings") == "LR"
assert slugify("  Hello, World! Python 101  ") == "hello-world-python-101"
assert slugify("My   First Blog Post!!") == "my-first-blog-post"
print("✅ All checks passed!")
