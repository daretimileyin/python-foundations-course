height = int(input("Height: "))

print("Pyramid:")
for i in range(1, height + 1):
    print(" " * (height - i) + "*" * (2 * i - 1))

print("\nUpside down:")
for i in range(height, 0, -1):
    print(" " * (height - i) + "*" * (2 * i - 1))

print("\nDiamond:")
for i in range(1, height + 1):
    print(" " * (height - i) + "*" * (2 * i - 1))
for i in range(height - 1, 0, -1):
    print(" " * (height - i) + "*" * (2 * i - 1))
