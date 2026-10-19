# Module 01 – Python Basics

## 🎯 Learning objectives
By the end of this module you will be able to:
- Display output with `print()`
- Store data in variables and choose good variable names
- Work with the basic data types: `int`, `float`, `str`, `bool`
- Get input from the user with `input()`
- Convert between types (`int()`, `float()`, `str()`)
- Use arithmetic, comparison and assignment operators
- Format text nicely with f-strings

---

## 📖 Concepts

### 1. `print()`
```python
print("Hello, world!")
print("Python", "is", "fun")        # Python is fun  (separated by spaces)
print("a", "b", "c", sep="-")        # a-b-c
print("No newline", end=" ")
print("after this")                   # No newline after this
```

### 2. Comments
```python
# This is a single-line comment

"""
This is a multi-line string,
often used as a multi-line comment or documentation.
"""
```

### 3. Variables
A variable is a **name** that points to a **value**.
```python
name = "Ada"
age = 25
height = 1.68
is_student = True
```
**Naming rules:**
- Letters, numbers and underscores only; can't start with a number
- Case-sensitive: `age` and `Age` are different
- Use `snake_case` for Python: `first_name`, not `firstName`
- Choose **meaningful** names: `price` beats `p`

### 4. Data types
| Type | Example | Description |
|------|---------|-------------|
| `int` | `42`, `-7` | Whole numbers |
| `float` | `3.14`, `-0.5` | Decimal numbers |
| `str` | `"hello"`, `'hi'` | Text (string) |
| `bool` | `True`, `False` | Yes/no values |
| `NoneType` | `None` | "Nothing" / no value |

Check a type with `type()`:
```python
print(type(42))       # <class 'int'>
print(type("42"))     # <class 'str'>
```

### 5. Arithmetic operators
| Operator | Meaning | Example | Result |
|----------|---------|---------|--------|
| `+` | add | `7 + 2` | `9` |
| `-` | subtract | `7 - 2` | `5` |
| `*` | multiply | `7 * 2` | `14` |
| `/` | divide | `7 / 2` | `3.5` |
| `//` | floor divide | `7 // 2` | `3` |
| `%` | remainder (modulo) | `7 % 2` | `1` |
| `**` | power | `7 ** 2` | `49` |

Order of operations follows maths (BODMAS/PEMDAS). Use brackets to be clear: `(2 + 3) * 4`.

### 6. Assignment shortcuts
```python
score = 10
score += 5     # same as score = score + 5  → 15
score -= 3     # 12
score *= 2     # 24
```

### 7. Strings basics
```python
first = "Ada"
last = "Lovelace"
full = first + " " + last        # concatenation → "Ada Lovelace"
laugh = "ha" * 3                  # "hahaha"
print(len(full))                  # 12 (number of characters)
```

### 8. f-strings (formatted strings) ⭐ use these a lot
```python
name = "Ada"
age = 25
print(f"My name is {name} and I am {age} years old.")
print(f"Next year I'll be {age + 1}.")
price = 3.14159
print(f"Price: {price:.2f}")      # Price: 3.14  (2 decimal places)
```

### 9. `input()`: getting data from the user
```python
name = input("What is your name? ")
print(f"Hello, {name}!")
```
⚠️ `input()` **always returns a string**, even if the user types a number!

### 10. Type conversion
```python
age_text = input("Your age: ")    # "25"  (a string)
age = int(age_text)               # 25    (an integer)
print(age + 1)                    # 26

int("42")      # 42
float("3.5")   # 3.5
str(100)       # "100"
int(3.9)       # 3  (cuts off the decimal, doesn't round)
round(3.9)     # 4
```

### 11. Comparison operators (produce `True`/`False`)
```python
5 == 5     # True   (equal; note TWO equals signs)
5 != 3     # True   (not equal)
5 > 3      # True
5 <= 3     # False
```

---

## 🧪 Examples
Run each one, read the code, then **change it** and run it again.

| File | Shows |
|------|-------|
| [`01_hello_world.py`](examples/01_hello_world.py) | `print()` options |
| [`02_variables_and_types.py`](examples/02_variables_and_types.py) | Variables, `type()` |
| [`03_operators.py`](examples/03_operators.py) | Arithmetic and comparisons |
| [`04_input_and_fstrings.py`](examples/04_input_and_fstrings.py) | `input()`, conversion, f-strings |

---

## ✍️ Exercises
Files are in [`exercises/`](exercises/). Solutions in [`solutions/`](solutions/) (try first!).

| # | File | Difficulty | Task |
|---|------|-----------|------|
| 1 | `ex01_greeting.py` | ⭐ | Ask for name and city, print a greeting |
| 2 | `ex02_age_calculator.py` | ⭐ | Calculate age in months, days and the year they turn 100 |
| 3 | `ex03_temperature.py` | ⭐⭐ | Convert Celsius ↔ Fahrenheit |
| 4 | `ex04_shopping_bill.py` | ⭐⭐ | Calculate a bill with tax and tip, formatted to 2 decimals |
| 5 | `ex05_time_converter.py` | ⭐⭐⭐ | Convert seconds into hours, minutes, seconds using `//` and `%` |

---

## 🛠️ Mini-project: Simple Calculator
Create `exercises/calculator.py` that:
1. Asks the user for two numbers (they might be decimals!)
2. Prints the result of `+`, `-`, `*`, `/`, `//`, `%` and `**` on them
3. Formats every result nicely, e.g. `7.0 + 2.0 = 9.00`

**Bonus:** also print which number is bigger using a comparison (you'll learn a better way in Module 02).

---

## ⚠️ Common mistakes
```python
age = input("Age: ")
print(age + 1)        # ❌ TypeError: can only concatenate str (not "int") to str
print(int(age) + 1)   # ✅
```
```python
print("Total: " + 10)       # ❌ TypeError
print("Total: " + str(10))  # ✅
print(f"Total: {10}")       # ✅✅ better
```
- `=` assigns, `==` compares.
- `print(Hello)` without quotes → `NameError`, because Python thinks `Hello` is a variable.
- Mismatched quotes: `"hello'` → `SyntaxError`.

## 🔗 Resources
- [Python docs: An Informal Introduction](https://docs.python.org/3/tutorial/introduction.html)
- [Real Python: Variables](https://realpython.com/python-variables/)
- [Real Python: f-strings](https://realpython.com/python-f-strings/)

## ✅ Checklist
- [ ] I can explain the difference between `int`, `float`, `str` and `bool`
- [ ] I know why `input()` needs converting before doing maths
- [ ] I can use `//` and `%` and explain what they do
- [ ] I can format output with f-strings, including `:.2f`
- [ ] I completed exercises 1–5 and the calculator
