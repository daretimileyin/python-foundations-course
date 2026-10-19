def safe_divide(a, b):
    try:
        return float(a) / float(b)
    except (ZeroDivisionError, ValueError, TypeError):
        return None


assert safe_divide(10, 2) == 5
assert safe_divide("9", "3") == 3
assert safe_divide(1, 0) is None
assert safe_divide("ten", 2) is None
print("✅ All checks passed!")
