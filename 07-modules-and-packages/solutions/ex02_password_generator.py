import secrets
import string


def generate_password(length=12, use_symbols=True):
    pool = string.ascii_letters + string.digits
    if use_symbols:
        pool += string.punctuation

    chars = [
        secrets.choice(string.ascii_uppercase),
        secrets.choice(string.ascii_lowercase),
        secrets.choice(string.digits),
    ]
    chars += [secrets.choice(pool) for _ in range(length - len(chars))]
    secrets.SystemRandom().shuffle(chars)
    return "".join(chars)


for _ in range(5):
    pw = generate_password()
    print(pw)
    assert len(pw) == 12
    assert any(c.isupper() for c in pw)
    assert any(c.islower() for c in pw)
    assert any(c.isdigit() for c in pw)
assert all(c.isalnum() for c in generate_password(20, use_symbols=False))
print("✅ All checks passed!")
