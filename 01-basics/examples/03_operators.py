"""Example 03 – Arithmetic and comparison operators."""

a = 17
b = 5

print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b}")
print(f"{a} // {b} = {a // b}   (how many whole times b fits into a)")
print(f"{a} % {b} = {a % b}    (what is left over)")
print(f"{a} ** 2 = {a ** 2}")

print()
print("Order of operations:")
print("2 + 3 * 4 =", 2 + 3 * 4)
print("(2 + 3) * 4 =", (2 + 3) * 4)

print()
print("Comparisons:")
print(f"{a} == {b} ->", a == b)
print(f"{a} != {b} ->", a != b)
print(f"{a} > {b}  ->", a > b)
print(f"{a} <= {b} ->", a <= b)

# A handy use of %: checking if a number is even
number = 42
print(f"Is {number} even?", number % 2 == 0)
