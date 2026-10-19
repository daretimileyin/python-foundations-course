"""
⭐⭐ Exercise 2 – Password Generator

Write generate_password(length=12, use_symbols=True) that returns a
random password containing letters (upper and lower), digits and,
optionally, symbols.

Guarantee at least one uppercase, one lowercase and one digit.

Useful:
    import string
    string.ascii_lowercase, string.ascii_uppercase, string.digits, string.punctuation
    random.choice(...), random.shuffle(...)

For real-world security use the `secrets` module instead of `random`.
Try switching to secrets.choice once it works!
"""
import random
import string


def generate_password(length=12, use_symbols=True):
    # TODO
    pass


for _ in range(5):
    pw = generate_password()
    print(pw)
    assert len(pw) == 12
    assert any(c.isupper() for c in pw)
    assert any(c.islower() for c in pw)
    assert any(c.isdigit() for c in pw)
assert all(c.isalnum() for c in generate_password(20, use_symbols=False))
print("✅ All checks passed!")
