"""Example 02 – Dictionaries."""

capitals = {"Nigeria": "Abuja", "Ghana": "Accra", "Kenya": "Nairobi"}

print(capitals["Ghana"])
print(capitals.get("France", "Unknown"))

capitals["France"] = "Paris"        # add
capitals["Nigeria"] = "Abuja 🇳🇬"   # update
print(capitals)

for country, capital in capitals.items():
    print(f"The capital of {country} is {capital}")

print("Countries:", list(capitals.keys()))

# Counting with a dictionary
votes = ["pizza", "rice", "pizza", "salad", "rice", "pizza"]
counts = {}
for vote in votes:
    counts[vote] = counts.get(vote, 0) + 1
print("\nVote counts:", counts)

# Nested data
library = {
    "1984": {"author": "George Orwell", "year": 1949, "available": True},
    "Things Fall Apart": {"author": "Chinua Achebe", "year": 1958, "available": False},
}
for title, info in library.items():
    status = "✅" if info["available"] else "❌"
    print(f"{status} {title} by {info['author']} ({info['year']})")
