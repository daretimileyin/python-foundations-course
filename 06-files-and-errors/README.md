# Module 06 – Files & Error Handling

## 🎯 Learning objectives
By the end of this module you will be able to:
- Read from and write to text files
- Use `with` so files are always closed
- Work with file paths using `pathlib`
- Read and write CSV files
- Read error messages (tracebacks)
- Handle errors with `try` / `except` / `else` / `finally`
- Raise your own errors and validate input

---

## 📖 Concepts

### 1. Opening files
```python
with open("notes.txt", "w") as file:     # "w" = write (creates/overwrites)
    file.write("First line\n")
    file.write("Second line\n")
```
`with` automatically **closes** the file, even if something goes wrong.

| Mode | Meaning |
|------|---------|
| `"r"` | read (default); error if file doesn't exist |
| `"w"` | write; **erases** existing content |
| `"a"` | append; adds to the end |
| `"x"` | create; error if it already exists |

### 2. Reading files
```python
with open("notes.txt") as file:
    content = file.read()           # whole file as one string

with open("notes.txt") as file:
    for line in file:               # one line at a time (memory-friendly)
        print(line.strip())

with open("notes.txt") as file:
    lines = file.readlines()        # list of lines
```
💡 Add `encoding="utf-8"` to `open()` to handle emojis and accents on every OS.

### 3. Paths with `pathlib`
```python
from pathlib import Path

folder = Path(__file__).parent          # folder this script lives in
data_file = folder / "data" / "scores.txt"
print(data_file.exists())
data_file.parent.mkdir(exist_ok=True)   # make the folder if missing
text = data_file.read_text(encoding="utf-8")
```
Using `Path(__file__).parent` means your script works no matter which folder you run it from.

### 4. CSV files
```python
import csv

with open("people.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["name", "age"])
    writer.writerow(["Ada", 36])

with open("people.csv") as f:
    for row in csv.DictReader(f):
        print(row["name"], row["age"])     # each row is a dict
```

### 5. Reading a traceback
```
Traceback (most recent call last):
  File "app.py", line 3, in <module>
    print(10 / number)
          ~~~^~~~~~~~
ZeroDivisionError: division by zero
```
Read it **from the bottom up**: the last line tells you **what** happened; the lines above tell you **where**.

### 6. Common exceptions
| Exception | Typical cause |
|-----------|---------------|
| `ValueError` | `int("hello")` |
| `TypeError` | `"5" + 5` |
| `ZeroDivisionError` | `10 / 0` |
| `IndexError` | `[1, 2][5]` |
| `KeyError` | `{"a": 1}["b"]` |
| `FileNotFoundError` | opening a file that doesn't exist |
| `NameError` | using a variable that doesn't exist |
| `AttributeError` | `"hi".push()` |

### 7. `try` / `except`
```python
try:
    age = int(input("Age: "))
except ValueError:
    print("Please enter a whole number.")
```

Full form:
```python
try:
    number = int(input("Number: "))
    result = 100 / number
except ValueError:
    print("That's not a number!")
except ZeroDivisionError:
    print("Can't divide by zero!")
else:
    print(f"Result: {result}")       # runs only if NO error happened
finally:
    print("Done.")                   # ALWAYS runs
```

Getting the error message:
```python
except FileNotFoundError as error:
    print(f"Problem: {error}")
```

⚠️ Avoid bare `except:` or `except Exception:` that hides every error. Catch the **specific** errors you expect.

### 8. Validation loop pattern
```python
def ask_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Whole numbers only, please.")
```

### 9. Raising errors
```python
def withdraw(balance, amount):
    if amount <= 0:
        raise ValueError("Amount must be positive")
    if amount > balance:
        raise ValueError("Insufficient funds")
    return balance - amount
```

### 10. Custom exceptions
```python
class InsufficientFundsError(Exception):
    pass

raise InsufficientFundsError("You only have $20")
```

---

## 🧪 Examples
| File | Shows |
|------|-------|
| [`01_reading_writing.py`](examples/01_reading_writing.py) | Writing, appending, reading, pathlib |
| [`02_csv_files.py`](examples/02_csv_files.py) | Writing and reading CSV |
| [`03_exceptions.py`](examples/03_exceptions.py) | try/except/else/finally, raising errors |

---

## ✍️ Exercises
| # | File | Difficulty | Task |
|---|------|-----------|------|
| 1 | `ex01_safe_input.py` | ⭐ | `ask_int` and `ask_float` that never crash |
| 2 | `ex02_safe_divide.py` | ⭐ | Division that handles bad input |
| 3 | `ex03_file_stats.py` | ⭐⭐ | Count lines, words and characters in a file |
| 4 | `ex04_grades_csv.py` | ⭐⭐ | Read a CSV and write a summary report |
| 5 | `ex05_custom_exceptions.py` | ⭐⭐⭐ | Validate an age with custom exceptions |

---

## 🛠️ Mini-project: Personal Journal
Create `exercises/journal.py`:
1. **Write entry**: asks for text and appends it to `journal.txt` with the date and time:
   ```python
   from datetime import datetime
   stamp = datetime.now().strftime("%Y-%m-%d %H:%M")
   ```
2. **Read all entries**: prints the whole journal (handle the file not existing yet!)
3. **Search entries**: show entries containing a word
4. **Quit**

**Bonus:** count how many entries exist; add a "delete all" option with a confirmation question.

---

## ⚠️ Common mistakes
- Opening with `"w"` when you meant `"a"`: your data is wiped!
- Relative paths: `open("data.txt")` looks in the folder you *ran* Python from, not where the script is. Use `Path(__file__).parent`.
- Forgetting `\n` when writing lines.
- Wrapping huge blocks of code in one `try`: keep `try` blocks small so you know what failed.
- Silencing errors with `except: pass`. You'll never know what went wrong.

## 🔗 Resources
- [Python docs: Reading and Writing Files](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)
- [Python docs: Errors and Exceptions](https://docs.python.org/3/tutorial/errors.html)
- [Real Python: pathlib](https://realpython.com/python-pathlib/)
- [Real Python: Exceptions](https://realpython.com/python-exceptions/)

## ✅ Checklist
- [ ] I know the difference between modes `r`, `w` and `a`
- [ ] I always use `with` to open files
- [ ] I can read a traceback from the bottom up
- [ ] I can catch specific exceptions
- [ ] I can raise my own errors
- [ ] I built the journal
