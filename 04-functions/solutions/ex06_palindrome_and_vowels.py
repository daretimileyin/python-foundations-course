def is_palindrome(text):
    cleaned = "".join(char.lower() for char in text if char.isalnum())
    return cleaned == cleaned[::-1]


def count_vowels(text):
    return sum(1 for char in text.lower() if char in "aeiou")


def capitalize_words(text):
    words = text.split(" ")
    return " ".join(word[:1].upper() + word[1:] for word in words)


assert is_palindrome("racecar") is True
assert is_palindrome("A man, a plan, a canal: Panama") is True
assert is_palindrome("python") is False
assert count_vowels("Hello World") == 3
assert capitalize_words("hello big world") == "Hello Big World"
print("✅ All checks passed!")
