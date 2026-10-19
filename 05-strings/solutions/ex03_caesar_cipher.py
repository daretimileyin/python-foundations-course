def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord("A") if char.isupper() else ord("a")
            position = ord(char) - base
            result += chr(base + (position + shift) % 26)
        else:
            result += char
    return result


def decrypt(text, shift):
    return encrypt(text, -shift)


assert encrypt("abc xyz", 3) == "def abc"
assert encrypt("Hello, World!", 5) == "Mjqqt, Btwqi!"
assert decrypt("Mjqqt, Btwqi!", 5) == "Hello, World!"
print("✅ All checks passed!")
