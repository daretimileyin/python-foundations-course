"""
⭐⭐ Exercise 3 – Caesar Cipher

Shift every letter forward in the alphabet by `shift` places, wrapping
around from z back to a. Keep the case. Leave other characters alone.

    encrypt("abc xyz", 3)  → "def abc"

Hints:
  - ord("a") is 97. Position in alphabet: ord(char) - ord("a")
  - new_position = (position + shift) % 26
  - decrypt is just encrypt with a negative shift!
"""


def encrypt(text, shift):
    # TODO
    pass


def decrypt(text, shift):
    # TODO
    pass


assert encrypt("abc xyz", 3) == "def abc"
assert encrypt("Hello, World!", 5) == "Mjqqt, Btwqi!"
assert decrypt("Mjqqt, Btwqi!", 5) == "Hello, World!"
print("✅ All checks passed!")
