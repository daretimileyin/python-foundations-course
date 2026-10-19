"""Mini-project solution – Simple Calculator."""

a = float(input("First number: "))
b = float(input("Second number: "))

print(f"{a} + {b} = {a + b:.2f}")
print(f"{a} - {b} = {a - b:.2f}")
print(f"{a} * {b} = {a * b:.2f}")
print(f"{a} / {b} = {a / b:.2f}")
print(f"{a} // {b} = {a // b:.2f}")
print(f"{a} % {b} = {a % b:.2f}")
print(f"{a} ** {b} = {a ** b:.2f}")

# Bonus
print(f"Is {a} bigger than {b}? {a > b}")
