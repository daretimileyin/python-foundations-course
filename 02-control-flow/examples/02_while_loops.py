"""Example 02 – while loops."""

# Countdown
count = 5
while count > 0:
    print(count)
    count -= 1
print("Liftoff! 🚀")

# Keep asking until the input is valid
number = int(input("Enter a number between 1 and 10: "))
while number < 1 or number > 10:
    print("That's out of range.")
    number = int(input("Enter a number between 1 and 10: "))
print(f"Thanks, you chose {number}.")

# Running total with an input loop
total = 0
while True:
    entry = input("Enter a number to add (or 'done'): ")
    if entry == "done":
        break
    total += float(entry)
    print(f"Running total: {total}")
print(f"Final total: {total}")
