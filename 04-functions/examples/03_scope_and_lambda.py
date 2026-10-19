"""Example 03 – Scope, lambdas and functions as values."""

counter = 0  # global


def increment(value):
    # 'value' is local; we return a new value instead of changing a global
    return value + 1


counter = increment(counter)
counter = increment(counter)
print("Counter:", counter)


def show_scope():
    message = "I only exist inside show_scope"
    print(message)


show_scope()
# print(message)   # ← uncomment to see a NameError

# Functions are values: you can store them and pass them around
def shout(text):
    return text.upper() + "!"


def whisper(text):
    return text.lower() + "..."


for style in [shout, whisper]:
    print(style("Hello there"))

# Lambdas
double = lambda n: n * 2
print("double(21) =", double(21))

words = ["banana", "Kiwi", "apple", "cherry"]
print("Sorted:", sorted(words))
print("Sorted ignoring case:", sorted(words, key=lambda w: w.lower()))
print("Sorted by length:", sorted(words, key=len))

numbers = [1, 2, 3, 4, 5, 6]
print("map (squares):", list(map(lambda n: n ** 2, numbers)))
print("filter (evens):", list(filter(lambda n: n % 2 == 0, numbers)))
