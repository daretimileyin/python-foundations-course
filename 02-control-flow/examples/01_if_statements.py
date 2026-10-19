"""Example 01 – Making decisions."""

age = int(input("How old are you? "))

if age < 0:
    print("That's not a real age!")
elif age < 13:
    print("You're a child.")
elif age < 20:
    print("You're a teenager.")
elif age < 65:
    print("You're an adult.")
else:
    print("You're a senior.")

# Combining conditions
has_ticket = input("Do you have a ticket? (y/n) ") == "y"

if age >= 18 and has_ticket:
    print("Welcome to the concert! 🎸")
elif age >= 18 and not has_ticket:
    print("Please buy a ticket first.")
else:
    print("Sorry, this concert is 18+.")

# Chained comparison
if 13 <= age <= 19:
    print("(Fun fact: you're a teen)")
