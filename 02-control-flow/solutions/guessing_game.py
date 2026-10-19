"""Mini-project solution – Number Guessing Game (with bonuses)."""
import random

while True:
    level = input("Choose difficulty – (e)asy or (h)ard: ").lower()
    top = 500 if level == "h" else 50
    max_guesses = 10 if level == "h" else 7

    secret = random.randint(1, top)
    print(f"\nI'm thinking of a number between 1 and {top}. You have {max_guesses} guesses.")

    guesses = 0
    while guesses < max_guesses:
        guess = int(input("Your guess: "))
        guesses += 1
        if guess < secret:
            print("Too low ⬇️")
        elif guess > secret:
            print("Too high ⬆️")
        else:
            print(f"🎉 You got it in {guesses} guesses!")
            break
    else:
        print(f"😢 Out of guesses! The number was {secret}.")

    if input("\nPlay again? (y/n) ").lower() != "y":
        print("Thanks for playing!")
        break
