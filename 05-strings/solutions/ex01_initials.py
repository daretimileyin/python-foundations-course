def get_initials(full_name):
    return "".join(word[0].upper() + "." for word in full_name.split())


assert get_initials("ada king lovelace") == "A.K.L."
assert get_initials("Alan Turing") == "A.T."
assert get_initials("  grace   hopper ") == "G.H."
print("✅ All checks passed!")
