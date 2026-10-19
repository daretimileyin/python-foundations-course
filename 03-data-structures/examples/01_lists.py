"""Example 01 – Lists."""

colours = ["red", "green", "blue"]
print("Start:", colours)

colours.append("yellow")
colours.insert(1, "orange")
print("After adding:", colours)

colours.remove("green")
popped = colours.pop()
print(f"Removed green and popped {popped}:", colours)

print("First:", colours[0], "| Last:", colours[-1])
print("Length:", len(colours))
print("Is 'blue' in the list?", "blue" in colours)

numbers = [5, 2, 9, 1, 7, 3]
print("\nNumbers:", numbers)
print("Slice [1:4]:", numbers[1:4])
print("Reversed:", numbers[::-1])
print("Sorted copy:", sorted(numbers))
print("Original is unchanged:", numbers)
numbers.sort()
print("Sorted in place:", numbers)
print(f"Sum={sum(numbers)}  Min={min(numbers)}  Max={max(numbers)}")
print(f"Average={sum(numbers) / len(numbers):.2f}")

print("\nNumbered list:")
for i, colour in enumerate(colours, start=1):
    print(f"{i}. {colour}")

# Building a list with a loop
squares = []
for n in range(1, 6):
    squares.append(n * n)
print("\nSquares:", squares)
