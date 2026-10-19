"""Example 03 – for loops and range()."""

print("Counting 1 to 5:")
for i in range(1, 6):
    print(i)

print("\nEven numbers to 10:")
for i in range(0, 11, 2):
    print(i, end=" ")
print()

print("\nLooping over a string:")
for char in "Hello":
    print(char)

print("\nSum of 1..100:")
total = 0
for i in range(1, 101):
    total += i
print(total)

print("\nbreak and continue:")
for n in range(1, 11):
    if n % 2 == 0:
        continue        # skip even numbers
    if n > 7:
        break           # stop when we pass 7
    print(n)

print("\nA small times table (nested loops):")
for row in range(1, 6):
    for col in range(1, 6):
        print(f"{row * col:4}", end="")
    print()
