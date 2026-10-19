"""
⭐⭐ Exercise 2 – Email Validator

Write is_valid_email(email) that returns True only if ALL are true:
  - it contains exactly one "@"
  - there is at least one character before the "@"
  - the part after the "@" contains a "." that is not the first or last character
  - there are no spaces
"""


def is_valid_email(email):
    # TODO
    pass


assert is_valid_email("ada@example.com") is True
assert is_valid_email("a.b@school.edu.ng") is True
assert is_valid_email("adaexample.com") is False
assert is_valid_email("@example.com") is False
assert is_valid_email("ada@@example.com") is False
assert is_valid_email("ada@example") is False
assert is_valid_email("ada@.com") is False
assert is_valid_email("ada lovelace@example.com") is False
print("✅ All checks passed!")
