CURRENT_YEAR = 2026

age = int(input("How old are you? "))

months = age * 12
days = age * 365
year_100 = CURRENT_YEAR + (100 - age)

print(f"You are {months} months old.")
print(f"You are about {days} days old.")
print(f"You will turn 100 in the year {year_100}.")
