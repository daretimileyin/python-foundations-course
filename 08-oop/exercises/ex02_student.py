"""
⭐⭐ Exercise 2 – Student

Create a Student class:
  - __init__(self, name)            → stores name and an empty list of grades
  - add_grade(grade)                → adds a grade; raise ValueError if not 0–100
  - average()                       → average grade (0 if there are none)
  - letter_grade()                  → A (90+), B (80+), C (70+), D (60+), F
  - __str__                         → "Ada: 87.5 (B)"
"""

# Write your class here 👇


s = Student("Ada")
assert s.average() == 0
s.add_grade(90)
s.add_grade(85)
assert s.average() == 87.5
assert s.letter_grade() == "B"
assert str(s) == "Ada: 87.5 (B)"
try:
    s.add_grade(150)
    assert False, "Should have raised ValueError"
except ValueError:
    pass
print("✅ All checks passed!")
