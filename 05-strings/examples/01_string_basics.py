"""Example 01 – String basics."""

text = "Python Programming"

print("Original:", text)
print("Length:", len(text))
print("First char:", text[0])
print("Last char:", text[-1])
print("First word:", text[:6])
print("Second word:", text[7:])
print("Every 2nd char:", text[::2])
print("Reversed:", text[::-1])

print("\nCase methods:")
print(text.upper(), "|", text.lower(), "|", text.swapcase())

print("\nSearching:")
print("'gram' in text?", "gram" in text)
print("Position of 'Pro':", text.find("Pro"))
print("Count of 'm':", text.count("m"))
print("Starts with 'Py'?", text.startswith("Py"))

print("\nChecks:")
for sample in ["hello", "12345", "hello123", "Hello World"]:
    print(f"{sample!r:15} alpha={sample.isalpha()} digit={sample.isdigit()} alnum={sample.isalnum()}")

print("\nImmutability:")
original = "cat"
changed = original.replace("c", "b")
print(f"original={original}  changed={changed}")
