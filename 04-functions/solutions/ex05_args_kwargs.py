def multiply_all(*numbers):
    result = 1
    for n in numbers:
        result *= n
    return result


def make_sentence(*words, ending="."):
    sentence = " ".join(words)
    return sentence[0].upper() + sentence[1:] + ending


def describe_pet(name, **details):
    parts = [f"{key}={value}" for key, value in details.items()]
    return f"{name}: " + ", ".join(parts)


assert multiply_all(2, 3, 4) == 24
assert multiply_all() == 1
assert make_sentence("python", "is", "fun") == "Python is fun."
assert make_sentence("are", "you", "ready", ending="?") == "Are you ready?"
assert describe_pet("Rex", species="dog", age=3) == "Rex: species=dog, age=3"
print("✅ All checks passed!")
