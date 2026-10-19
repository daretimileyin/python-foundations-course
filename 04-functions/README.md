# Module 04 – Functions

## 🎯 Learning objectives
By the end of this module you will be able to:
- Define and call your own functions
- Pass information in with **parameters** and get results back with `return`
- Use default values, keyword arguments, `*args` and `**kwargs`
- Understand **scope** (local vs global variables)
- Write docstrings and type hints
- Use small anonymous functions (`lambda`)
- Break a big problem into small functions

---

## 📖 Concepts

### 1. Why functions?
Functions let you **name** a piece of code and **reuse** it. They follow the **DRY** principle: *Don't Repeat Yourself*.

### 2. Defining and calling
```python
def greet():
    print("Hello!")

greet()     # call it
greet()     # reuse it
```

### 3. Parameters and arguments
```python
def greet(name):            # name is a PARAMETER
    print(f"Hello, {name}!")

greet("Ada")                # "Ada" is an ARGUMENT
```

### 4. `return`: sending a value back
```python
def add(a, b):
    return a + b

result = add(3, 4)    # 7
print(add(10, 5))     # 15
```
`print` **shows** a value; `return` **gives it back** so you can use it. A function without `return` returns `None`.

`return` ends the function immediately:
```python
def is_adult(age):
    if age >= 18:
        return True
    return False        # (or simply: return age >= 18)
```

Returning several values (as a tuple):
```python
def min_max(numbers):
    return min(numbers), max(numbers)

low, high = min_max([4, 9, 1])
```

### 5. Default values and keyword arguments
```python
def power(base, exponent=2):
    return base ** exponent

power(5)                  # 25 (uses default)
power(5, 3)               # 125
power(exponent=3, base=2) # 8  (keyword arguments, any order)
```

### 6. `*args` and `**kwargs`
```python
def total(*numbers):              # any number of positional args → tuple
    return sum(numbers)
total(1, 2, 3, 4)                 # 10

def profile(**info):              # any number of keyword args → dict
    for key, value in info.items():
        print(f"{key}: {value}")
profile(name="Ada", job="Engineer")
```

### 7. Scope
```python
x = "global"

def show():
    x = "local"        # a NEW variable that only exists inside the function
    print(x)

show()     # local
print(x)   # global
```
Variables created inside a function disappear when it ends. Pass data **in** with parameters and **out** with `return`; avoid `global`.

### 8. Docstrings and type hints
```python
def area_of_circle(radius: float) -> float:
    """Return the area of a circle with the given radius."""
    return 3.14159 * radius ** 2

help(area_of_circle)   # shows the docstring
```
Type hints (`: float`, `-> float`) don't change how the code runs. They document it and help VS Code catch mistakes.

### 9. Lambda functions
Tiny one-line functions, often used with `sorted()`, `map()`, `filter()`:
```python
square = lambda n: n ** 2
square(4)    # 16

people = [("Ada", 36), ("Alan", 41), ("Grace", 29)]
sorted(people, key=lambda person: person[1])   # sort by age
```

### 10. The `main()` pattern
```python
def main():
    name = input("Name: ")
    print(greet(name))

if __name__ == "__main__":
    main()
```
This means *"only run `main()` when this file is run directly, not when it's imported"* (more in Module 07).

---

## 🧪 Examples
| File | Shows |
|------|-------|
| [`01_defining_functions.py`](examples/01_defining_functions.py) | def, parameters, return |
| [`02_arguments.py`](examples/02_arguments.py) | Defaults, keyword args, `*args`, `**kwargs` |
| [`03_scope_and_lambda.py`](examples/03_scope_and_lambda.py) | Scope, lambdas, functions as values |

---

## ✍️ Exercises
Each exercise has a function to complete plus some `assert` checks at the bottom. If you run the file and see **no errors**, your function works! ✅

| # | File | Difficulty | Task |
|---|------|-----------|------|
| 1 | `ex01_basic_functions.py` | ⭐ | `square`, `is_even`, `full_name` |
| 2 | `ex02_bmi.py` | ⭐ | Calculate BMI and its category |
| 3 | `ex03_list_functions.py` | ⭐⭐ | `average`, `count_above`, `only_positive` |
| 4 | `ex04_prime_numbers.py` | ⭐⭐ | `is_prime` and `primes_up_to` |
| 5 | `ex05_args_kwargs.py` | ⭐⭐ | Functions using `*args` and `**kwargs` |
| 6 | `ex06_palindrome_and_vowels.py` | ⭐⭐⭐ | `is_palindrome`, `count_vowels`, `capitalize_words` |

> 💡 `assert something` does nothing if `something` is True, and crashes with `AssertionError` if it's False. It's a mini-test. You'll learn proper testing in Module 09.

---

## 🛠️ Mini-project: Unit Converter
Create `exercises/unit_converter.py` with one function per conversion:
- `km_to_miles(km)`, `miles_to_km(miles)`
- `kg_to_pounds(kg)`, `pounds_to_kg(lb)`
- `celsius_to_fahrenheit(c)`, `fahrenheit_to_celsius(f)`

Then a `main()` function that shows a menu, asks for the conversion and value, and prints the result. Keep looping until the user chooses *quit*.

**Bonus:** store the functions in a dictionary, e.g. `{"1": ("km → miles", km_to_miles), ...}`, so the menu builds itself.

---

## ⚠️ Common mistakes
- Forgetting the brackets: `greet` refers to the function; `greet()` calls it.
- Using `print` instead of `return`, then getting `None` when you try to use the result.
- Code after `return` never runs.
- **Mutable default arguments:** `def add(item, items=[])` ❌ shares one list between calls. Use `items=None` and create the list inside.
- Defining a function *after* the line that calls it (in a script, define first).

## 🔗 Resources
- [Python docs: Defining Functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)
- [Real Python: Defining Your Own Function](https://realpython.com/defining-your-own-python-function/)
- [Real Python: *args and **kwargs](https://realpython.com/python-kwargs-and-args/)

## ✅ Checklist
- [ ] I can explain the difference between `print` and `return`
- [ ] I can write a function with a default parameter
- [ ] I understand local vs global scope
- [ ] I can sort a list using `key=lambda ...`
- [ ] All `assert`s pass in my exercises
- [ ] I built the unit converter
