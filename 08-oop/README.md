# Module 08 – Object-Oriented Programming (OOP)

## 🎯 Learning objectives
By the end of this module you will be able to:
- Explain what classes and objects are
- Write classes with `__init__`, attributes and methods
- Understand `self`
- Use class attributes vs instance attributes
- Use special ("dunder") methods like `__str__`, `__repr__`, `__eq__`
- Reuse code with **inheritance** and `super()`
- Protect data with properties and naming conventions
- Use `@dataclass` to write simple classes quickly

---

## 📖 Concepts

### 1. Classes and objects
A **class** is a blueprint. An **object** (or *instance*) is something built from that blueprint.
```python
class Dog:
    def __init__(self, name, age):
        self.name = name       # attribute
        self.age = age

    def bark(self):            # method
        return f"{self.name} says Woof!"

rex = Dog("Rex", 3)            # create an object
print(rex.name)                # Rex
print(rex.bark())              # Rex says Woof!
```
- `__init__` runs automatically when an object is created (the *constructor*).
- `self` means "this particular object". Python passes it automatically.

### 2. Changing state with methods
```python
class Counter:
    def __init__(self):
        self.count = 0

    def increment(self, by=1):
        self.count += by

c = Counter()
c.increment()
c.increment(5)
print(c.count)    # 6
```

### 3. Class attributes vs instance attributes
```python
class Circle:
    pi = 3.14159              # class attribute (shared by all circles)

    def __init__(self, radius):
        self.radius = radius  # instance attribute (one per circle)

    def area(self):
        return Circle.pi * self.radius ** 2
```

### 4. Dunder (double-underscore) methods
```python
class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __str__(self):              # used by print() and str()
        return f"'{self.title}' ({self.pages} pages)"

    def __repr__(self):             # used in the REPL / debugging
        return f"Book({self.title!r}, {self.pages})"

    def __len__(self):              # len(book)
        return self.pages

    def __eq__(self, other):        # book1 == book2
        return self.title == other.title
```

### 5. Inheritance
A child class gets everything from its parent and can add or change things.
```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "..."

class Cat(Animal):
    def speak(self):                 # override
        return "Meow"

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)       # run the parent's __init__
        self.breed = breed

    def speak(self):
        return "Woof"

for pet in [Cat("Tom"), Dog("Rex", "Lab")]:
    print(pet.name, pet.speak())     # polymorphism: same call, different behaviour
```
`isinstance(rex, Animal)` → `True`

### 6. Encapsulation and properties
By convention a leading underscore means *"internal, please don't touch"*:
```python
class BankAccount:
    def __init__(self, owner):
        self.owner = owner
        self._balance = 0

    @property
    def balance(self):            # read like an attribute: account.balance
        return self._balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit must be positive")
        self._balance += amount
```

### 7. Class methods and static methods
```python
class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    @classmethod
    def from_fahrenheit(cls, f):           # alternative constructor
        return cls((f - 32) * 5 / 9)

    @staticmethod
    def is_freezing(celsius):              # utility; needs no self/cls
        return celsius <= 0

t = Temperature.from_fahrenheit(212)
```

### 8. Dataclasses
For classes that mainly hold data, `@dataclass` writes `__init__`, `__repr__` and `__eq__` for you:
```python
from dataclasses import dataclass

@dataclass
class Point:
    x: float
    y: float

p = Point(3, 4)
print(p)              # Point(x=3, y=4)
```

### 9. When to use OOP?
Use a class when you have **data and behaviour that belong together**: a bank account (balance + deposit/withdraw), a player in a game (health + attack), a shopping cart (items + total). Not everything needs to be a class; functions are fine for simple tasks.

---

## 🧪 Examples
| File | Shows |
|------|-------|
| [`01_classes_basics.py`](examples/01_classes_basics.py) | Classes, `__init__`, methods, `self` |
| [`02_dunder_methods.py`](examples/02_dunder_methods.py) | `__str__`, `__repr__`, `__eq__`, `__len__`, `__add__` |
| [`03_inheritance.py`](examples/03_inheritance.py) | Inheritance, `super()`, polymorphism |
| [`04_properties_dataclasses.py`](examples/04_properties_dataclasses.py) | `@property`, `@classmethod`, `@dataclass` |

---

## ✍️ Exercises
| # | File | Difficulty | Task |
|---|------|-----------|------|
| 1 | `ex01_rectangle.py` | ⭐ | A `Rectangle` class with area and perimeter |
| 2 | `ex02_student.py` | ⭐⭐ | A `Student` class with grades and an average |
| 3 | `ex03_shapes_inheritance.py` | ⭐⭐ | `Shape` → `Circle`, `Square`, `Triangle` |
| 4 | `ex04_shopping_cart.py` | ⭐⭐⭐ | `Product` and `ShoppingCart` working together |

---

## 🛠️ Mini-project: Bank Account System
Create `exercises/bank.py`:
- `BankAccount` with `owner`, a private `_balance`, a `balance` property, `deposit()`, `withdraw()` and a `history` list of transactions
- `withdraw()` raises a custom `InsufficientFundsError` when there isn't enough money
- `SavingsAccount(BankAccount)` with an `interest_rate` and `add_interest()` method
- `__str__` that shows the owner and balance
- A menu-driven `main()` to create an account, deposit, withdraw, view balance and view history

**Bonus:** a `Bank` class that holds many accounts and can `transfer(from_acc, to_acc, amount)`.

---

## ⚠️ Common mistakes
- Forgetting `self` in method definitions: `def bark():` → `TypeError: takes 0 positional arguments but 1 was given`
- Forgetting `self.` when using attributes: `name` instead of `self.name` → `NameError`
- Calling the class instead of creating an object: `Dog.bark()` vs `rex.bark()`
- Forgetting `super().__init__(...)` in a child class, so parent attributes are missing
- Typo in `__init__` (e.g. `__int__` or `_init_`). Python won't complain, but it won't run either!

## 🔗 Resources
- [Python docs: Classes](https://docs.python.org/3/tutorial/classes.html)
- [Real Python: OOP in Python](https://realpython.com/python3-object-oriented-programming/)
- [Real Python: Dataclasses](https://realpython.com/python-data-classes/)

## ✅ Checklist
- [ ] I can explain class vs object and what `self` is
- [ ] I can write `__init__` and methods
- [ ] I can make `print(my_object)` look nice
- [ ] I can create a child class and use `super()`
- [ ] I know what `@property` and `@dataclass` do
- [ ] I built the bank account system
