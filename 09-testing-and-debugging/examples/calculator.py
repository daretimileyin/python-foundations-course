"""A small module we will test in test_calculator.py."""


def add(a, b):
    return a + b


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b


def is_even(n):
    return n % 2 == 0


class Calculator:
    """Remembers a running total and its history."""

    def __init__(self):
        self.total = 0
        self.history = []

    def apply(self, operation, value):
        if operation == "+":
            self.total += value
        elif operation == "-":
            self.total -= value
        elif operation == "*":
            self.total *= value
        else:
            raise ValueError(f"Unknown operation: {operation}")
        self.history.append((operation, value))
        return self.total
