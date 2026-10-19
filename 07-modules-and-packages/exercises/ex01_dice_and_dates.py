"""
⭐ Exercise 1 – Dice and Dates

1. Simulate rolling two dice 1000 times. Using a dictionary or Counter,
   print how often each total (2–12) appeared. Which is most common? Why?
2. Ask the user for their birthday (YYYY-MM-DD) and print:
     - which day of the week they were born on
     - how many days old they are
     - how many days until their next birthday
   Hint: datetime.strptime(text, "%Y-%m-%d").date()
"""
import random
from collections import Counter
from datetime import date, datetime

# Write your code here 👇
