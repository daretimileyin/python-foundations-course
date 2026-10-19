number = int(input("Which times table? "))
limit = int(input("Up to? "))

for i in range(1, limit + 1):
    print(f"{number} x {i} = {number * i}")
