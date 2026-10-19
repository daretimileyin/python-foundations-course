"""Example 01 – A tour of the standard library."""
import math
import random
from collections import Counter
from datetime import date, datetime, timedelta

print("🎲 Dice roll:", random.randint(1, 6))
print("🃏 Random choice:", random.choice(["rock", "paper", "scissors"]))
deck = list(range(1, 11))
random.shuffle(deck)
print("🔀 Shuffled:", deck)
print("🎯 Sample of 3:", random.sample(deck, 3))

print("\n√144 =", math.sqrt(144))
print("π =", round(math.pi, 5))
print("ceil(4.1) =", math.ceil(4.1), "| floor(4.9) =", math.floor(4.9))
print("5! =", math.factorial(5))

now = datetime.now()
print("\nNow:", now.strftime("%A %d %B %Y, %H:%M"))
today = date.today()
print("In 30 days:", today + timedelta(days=30))
new_year = date(today.year + 1, 1, 1)
print("Days until New Year:", (new_year - today).days)

letters = Counter("mississippi")
print("\nLetter counts:", letters)
print("Most common 2:", letters.most_common(2))
