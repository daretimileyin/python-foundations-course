def is_valid_email(email):
    if " " in email or email.count("@") != 1:
        return False
    local, domain = email.split("@")
    if not local:
        return False
    dot = domain.find(".")
    return dot > 0 and not domain.endswith(".")


assert is_valid_email("ada@example.com") is True
assert is_valid_email("a.b@school.edu.ng") is True
assert is_valid_email("adaexample.com") is False
assert is_valid_email("@example.com") is False
assert is_valid_email("ada@@example.com") is False
assert is_valid_email("ada@example") is False
assert is_valid_email("ada@.com") is False
assert is_valid_email("ada lovelace@example.com") is False
print("✅ All checks passed!")
