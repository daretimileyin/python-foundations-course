SMALL_WORDS = {"of", "and", "the"}


def make_acronym(phrase):
    return "".join(word[0].upper() for word in phrase.split() if word.lower() not in SMALL_WORDS)


def slugify(title):
    cleaned = "".join(ch for ch in title.lower() if ch.isalnum() or ch.isspace())
    return "-".join(cleaned.split())


assert make_acronym("portable network graphics") == "PNG"
assert make_acronym("Bank of America") == "BA"
assert make_acronym("the lord of the rings") == "LR"
assert slugify("  Hello, World! Python 101  ") == "hello-world-python-101"
assert slugify("My   First Blog Post!!") == "my-first-blog-post"
print("✅ All checks passed!")
