"""Example 03 – Inheritance and polymorphism."""


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def role(self):
        return "Employee"

    def annual_pay(self):
        return self.salary * 12

    def __str__(self):
        return f"{self.name} ({self.role()}): {self.annual_pay():,} per year"


class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size

    def role(self):
        return f"Manager of {self.team_size}"

    def annual_pay(self):
        bonus = 1000 * self.team_size
        return super().annual_pay() + bonus


class Intern(Employee):
    def role(self):
        return "Intern"

    def annual_pay(self):
        return self.salary * 6   # 6-month internship


staff = [Employee("Ada", 5000), Manager("Grace", 8000, 5), Intern("Alan", 2000)]

for person in staff:
    print(person)    # the same call behaves differently: polymorphism

print("\nIs Grace an Employee?", isinstance(staff[1], Employee))
print("Is Ada a Manager?", isinstance(staff[0], Manager))
print("Total payroll:", f"{sum(p.annual_pay() for p in staff):,}")
