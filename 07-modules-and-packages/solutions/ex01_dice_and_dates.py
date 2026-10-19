import random
from collections import Counter
from datetime import date, datetime

rolls = Counter(random.randint(1, 6) + random.randint(1, 6) for _ in range(1000))
for total in range(2, 13):
    print(f"{total:>2}: {'█' * (rolls[total] // 5)} {rolls[total]}")
print("Most common:", rolls.most_common(1)[0][0], "(7 has the most dice combinations: 6 of 36)")

birthday = datetime.strptime(input("\nBirthday (YYYY-MM-DD): "), "%Y-%m-%d").date()
today = date.today()
print("You were born on a", birthday.strftime("%A"))
print("Days old:", (today - birthday).days)

next_bday = birthday.replace(year=today.year)
if next_bday < today:
    next_bday = next_bday.replace(year=today.year + 1)
print("Days until next birthday:", (next_bday - today).days)
