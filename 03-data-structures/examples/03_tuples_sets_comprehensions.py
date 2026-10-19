"""Example 03 – Tuples, sets and comprehensions."""

# Tuples
rgb = (255, 128, 0)
red, green, blue = rgb
print(f"Red={red} Green={green} Blue={blue}")

# Returning multiple things is really a tuple
point = 3, 4
print(type(point), point)

# Sets
python_devs = {"Ada", "Alan", "Grace"}
js_devs = {"Grace", "Linus", "Ada"}
print("\nKnow both:", python_devs & js_devs)
print("Know either:", python_devs | js_devs)
print("Only Python:", python_devs - js_devs)

# Comprehensions
print("\nSquares:", [n ** 2 for n in range(1, 11)])
print("Odd numbers:", [n for n in range(20) if n % 2 == 1])
words = ["python", "is", "really", "fun"]
print("Long words:", [w for w in words if len(w) > 3])
print("Word lengths:", {w: len(w) for w in words})
print("Unique first letters:", {w[0] for w in words})
