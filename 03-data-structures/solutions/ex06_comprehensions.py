result1 = [n ** 2 for n in range(21) if n % 2 == 0]
print(result1)

names = ["ada", "bob", "chioma", "ed", "fatima"]
result2 = [name.upper() for name in names if len(name) > 3]
print(result2)

result3 = {n: n ** 3 for n in range(1, 6)}
print(result3)

matrix = [[1, 2], [3, 4], [5, 6]]
result4 = [value for row in matrix for value in row]
print(result4)
