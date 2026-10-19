class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grade(self, grade):
        if not 0 <= grade <= 100:
            raise ValueError("Grade must be between 0 and 100")
        self.grades.append(grade)

    def average(self):
        return sum(self.grades) / len(self.grades) if self.grades else 0

    def letter_grade(self):
        avg = self.average()
        for minimum, letter in [(90, "A"), (80, "B"), (70, "C"), (60, "D")]:
            if avg >= minimum:
                return letter
        return "F"

    def __str__(self):
        return f"{self.name}: {self.average()} ({self.letter_grade()})"


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
