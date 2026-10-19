"""
⭐⭐ Exercise 4 – Password Strength

Score a password: +1 point for each rule it meets:
  1. at least 8 characters
  2. contains a lowercase letter
  3. contains an uppercase letter
  4. contains a digit
  5. contains a symbol (anything that is not a letter or digit)

Return:
    0–2 points → "Weak"
    3–4 points → "Medium"
    5 points   → "Strong"

Hint: any(char.isdigit() for char in password)
"""


def password_strength(password):
    # TODO
    pass


assert password_strength("abc") == "Weak"
assert password_strength("abcdefgh") == "Weak"
assert password_strength("Abcdefgh1") == "Medium"
assert password_strength("Abcdefg1!") == "Strong"
print("✅ All checks passed!")
