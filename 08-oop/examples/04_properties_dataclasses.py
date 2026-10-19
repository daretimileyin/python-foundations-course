"""Example 04 – Properties, class methods and dataclasses."""
from dataclasses import dataclass, field


class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius        # goes through the setter below

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Below absolute zero!")
        self._celsius = value

    @property
    def fahrenheit(self):             # computed, read-only
        return self._celsius * 9 / 5 + 32

    @classmethod
    def from_fahrenheit(cls, f):
        return cls((f - 32) * 5 / 9)


t = Temperature(25)
print(f"{t.celsius}°C = {t.fahrenheit}°F")
t.celsius = 100
print(f"{t.celsius}°C = {t.fahrenheit}°F")
boiling = Temperature.from_fahrenheit(212)
print("212°F in °C:", boiling.celsius)
try:
    t.celsius = -300
except ValueError as e:
    print("Error:", e)


@dataclass
class Task:
    title: str
    priority: int = 1
    done: bool = False
    tags: list = field(default_factory=list)

    def complete(self):
        self.done = True


tasks = [Task("Learn OOP", 3, tags=["python"]), Task("Buy milk"), Task("Push to GitHub", 2)]
tasks[1].complete()
for task in sorted(tasks, key=lambda t: t.priority, reverse=True):
    print(task)
print("Equal?", Task("A") == Task("A"))
