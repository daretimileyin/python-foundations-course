"""Example 02 – Splitting, joining, cleaning and formatting."""

csv_line = "Ada,Lovelace,1815,London"
parts = csv_line.split(",")
print("Parts:", parts)
first, last, year, city = parts
print(f"{first} {last} was born in {city} in {year}.")

words = ["Python", "is", "awesome"]
print(" ".join(words))
print(" 🐍 ".join(words))

# Cleaning messy user input
answer = "   YeS  "
if answer.strip().lower() == "yes":
    print("\nThe user said yes (after cleaning).")

# Removing punctuation
sentence = "Hello, world! How's it going?"
cleaned = "".join(ch for ch in sentence if ch.isalnum() or ch.isspace())
print("Cleaned:", cleaned)

# A formatted table
products = [("Bread", 1.2, 3), ("Milk", 0.99, 2), ("Chocolate bar", 2.5, 1)]
print(f"\n{'Product':<15}{'Price':>8}{'Qty':>5}{'Total':>9}")
print("-" * 37)
grand_total = 0
for name, price, qty in products:
    total = price * qty
    grand_total += total
    print(f"{name:<15}{price:>8.2f}{qty:>5}{total:>9.2f}")
print("-" * 37)
print(f"{'GRAND TOTAL':<28}{grand_total:>9.2f}")
