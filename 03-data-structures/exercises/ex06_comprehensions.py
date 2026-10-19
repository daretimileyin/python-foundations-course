"""
⭐⭐⭐ Exercise 6 – Comprehensions

Rewrite each loop as a ONE-LINE comprehension. Print both results to
check they match.
"""

# 1. Squares of even numbers from 0 to 20
result1 = []
for n in range(21):
    if n % 2 == 0:
        result1.append(n ** 2)
# TODO: comprehension version

# 2. Uppercase names longer than 3 letters
names = ["ada", "bob", "chioma", "ed", "fatima"]
result2 = []
for name in names:
    if len(name) > 3:
        result2.append(name.upper())
# TODO: comprehension version

# 3. A dictionary mapping each number 1–5 to its cube
result3 = {}
for n in range(1, 6):
    result3[n] = n ** 3
# TODO: dictionary comprehension version

# 4. Flatten a list of lists
matrix = [[1, 2], [3, 4], [5, 6]]
result4 = []
for row in matrix:
    for value in row:
        result4.append(value)
# TODO: comprehension version (hint: two `for`s in one comprehension)
