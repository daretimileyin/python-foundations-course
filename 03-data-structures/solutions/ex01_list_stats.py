temperatures = [22.5, 19.0, 25.3, 30.1, 18.7, 27.4, 21.0]

print("Count:", len(temperatures))
print("Total:", sum(temperatures))
print(f"Average: {sum(temperatures) / len(temperatures):.2f}")
print("Min:", min(temperatures), "Max:", max(temperatures))
print("High to low:", sorted(temperatures, reverse=True))

# Without built-ins
total = 0
smallest = temperatures[0]
largest = temperatures[0]
for t in temperatures:
    total += t
    if t < smallest:
        smallest = t
    if t > largest:
        largest = t
print(f"\n(manual) Total={total:.1f} Avg={total / len(temperatures):.2f} Min={smallest} Max={largest}")
