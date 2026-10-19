"""
Debugger practice 🐛

This program should print the average of the positive numbers and the
largest number, but the output is wrong. Don't just read the code:
set a breakpoint on the first line of `analyse` and step through it
with F10, watching the variables.

(The answers are at the bottom of this file. Scroll down only after trying!)
"""


def analyse(numbers):
    positives = []
    for n in numbers:
        if n > 0:
            positives.append(n)

    total = 0
    for p in positives:
        total = p                      # 🐛

    average = total / len(numbers)     # 🐛

    largest = 0                        # 🐛 (what if all numbers are negative?)
    for n in numbers:
        if n > largest:
            largest = n

    return average, largest


print(analyse([4, -2, 8, 0, 6]))      # should print (6.0, 8)
print(analyse([-5, -1, -9]))          # largest should be -1









# ANSWERS
# 1. total = p   should be   total += p
# 2. divide by len(positives), not len(numbers) (and handle no positives!)
# 3. largest should start as numbers[0] (or use max(numbers))
