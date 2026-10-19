numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

# 1. Using a set (order is NOT guaranteed)
print("Set:", set(numbers))

# 2. Keeping order
seen = set()
unique = []
for n in numbers:
    if n not in seen:
        seen.add(n)
        unique.append(n)
print("Ordered unique:", unique)

# 3. Duplicates
duplicates = {n for n in numbers if numbers.count(n) > 1}
print("Appeared more than once:", sorted(duplicates))
