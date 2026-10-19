"""Example 04 – Getting input, converting types and formatting output."""

name = input("What's your name? ")
age = int(input("How old are you? "))
height = float(input("How tall are you in metres? "))

print(f"\nNice to meet you, {name}!")
print(f"In 10 years you'll be {age + 10}.")
print(f"Your height in centimetres is {height * 100:.0f} cm.")

# Formatting tricks
pi = 3.14159265
print(f"Pi to 2 places: {pi:.2f}")
print(f"Big number with commas: {1234567:,}")
print(f"Percentage: {0.256:.1%}")
print(f"Padded: [{name:>10}]")   # right-align in 10 characters
print(f"Padded: [{name:<10}]")   # left-align
print(f"Padded: [{name:^10}]")   # centre
