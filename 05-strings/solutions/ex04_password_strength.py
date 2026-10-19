def password_strength(password):
    score = 0
    if len(password) >= 8:
        score += 1
    if any(c.islower() for c in password):
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(not c.isalnum() for c in password):
        score += 1

    if score <= 2:
        return "Weak"
    if score <= 4:
        return "Medium"
    return "Strong"


assert password_strength("abc") == "Weak"
assert password_strength("abcdefgh") == "Weak"
assert password_strength("Abcdefgh1") == "Medium"
assert password_strength("Abcdefg1!") == "Strong"
print("✅ All checks passed!")
