# Module 02 – Control Flow

## 🎯 Learning objectives
By the end of this module you will be able to:
- Make decisions with `if`, `elif` and `else`
- Combine conditions with `and`, `or`, `not`
- Repeat code with `while` and `for` loops
- Use `range()` to loop a set number of times
- Control loops with `break` and `continue`
- Understand indentation and code blocks

---

## 📖 Concepts

### 1. Indentation matters!
Python uses **indentation** (4 spaces) to group code into blocks. A colon `:` starts a block.
```python
if True:
    print("This is inside the if")   # indented → inside the block
print("This is outside")              # not indented → always runs
```

### 2. `if` / `elif` / `else`
```python
temperature = 28

if temperature > 30:
    print("It's hot! 🥵")
elif temperature > 20:
    print("It's warm 🙂")
elif temperature > 10:
    print("It's cool 🧥")
else:
    print("It's cold 🥶")
```
Python checks each condition **top to bottom** and runs only the **first** one that's `True`.

### 3. Logical operators
| Operator | True when… | Example |
|----------|-----------|---------|
| `and` | both are true | `age >= 18 and has_ticket` |
| `or` | at least one is true | `day == "Sat" or day == "Sun"` |
| `not` | flips the value | `not is_raining` |

```python
age = 20
has_id = True
if age >= 18 and has_id:
    print("You may enter")
```
Chained comparisons work too: `if 0 <= score <= 100:`

### 4. Truthy and falsy
These count as `False` in a condition: `False`, `0`, `0.0`, `""` (empty string), `None`, `[]`, `{}`.
Everything else counts as `True`.
```python
name = input("Name: ")
if name:
    print(f"Hi {name}")
else:
    print("You didn't type anything!")
```

### 5. `while` loops: repeat *while* a condition is true
```python
count = 1
while count <= 5:
    print(count)
    count += 1       # ⚠️ forget this and the loop runs forever!
```

### 6. `for` loops: repeat for each item
```python
for letter in "Python":
    print(letter)

for number in range(5):          # 0, 1, 2, 3, 4
    print(number)
```

### 7. `range()`
| Call | Produces |
|------|----------|
| `range(5)` | 0, 1, 2, 3, 4 |
| `range(1, 6)` | 1, 2, 3, 4, 5 |
| `range(0, 10, 2)` | 0, 2, 4, 6, 8 |
| `range(10, 0, -1)` | 10, 9, … 1 |

The end number is **never included**.

### 8. `break` and `continue`
```python
for n in range(1, 11):
    if n == 3:
        continue     # skip the rest of this loop, go to the next n
    if n == 7:
        break        # exit the loop completely
    print(n)         # prints 1, 2, 4, 5, 6
```

### 9. The "input loop" pattern
```python
while True:
    answer = input("Type 'quit' to stop: ")
    if answer == "quit":
        break
    print(f"You typed {answer}")
```

### 10. Nested loops
```python
for row in range(1, 4):
    for col in range(1, 4):
        print(row * col, end="\t")
    print()
```

---

## 🧪 Examples
| File | Shows |
|------|-------|
| [`01_if_statements.py`](examples/01_if_statements.py) | `if/elif/else`, logical operators |
| [`02_while_loops.py`](examples/02_while_loops.py) | `while`, input loops |
| [`03_for_loops.py`](examples/03_for_loops.py) | `for`, `range`, `break`, `continue`, nested loops |

---

## ✍️ Exercises
| # | File | Difficulty | Task |
|---|------|-----------|------|
| 1 | `ex01_even_or_odd.py` | ⭐ | Say whether a number is even or odd |
| 2 | `ex02_grade_calculator.py` | ⭐ | Convert a score (0–100) into a letter grade |
| 3 | `ex03_fizzbuzz.py` | ⭐⭐ | The classic FizzBuzz |
| 4 | `ex04_multiplication_table.py` | ⭐⭐ | Print the times table for any number |
| 5 | `ex05_password_checker.py` | ⭐⭐ | Give the user 3 attempts to enter the password |
| 6 | `ex06_pyramid.py` | ⭐⭐⭐ | Print a pyramid of stars with nested loops |

---

## 🛠️ Mini-project: Number Guessing Game
Create `exercises/guessing_game.py`:
1. The computer picks a random number from 1 to 100:
   ```python
   import random
   secret = random.randint(1, 100)
   ```
2. The user keeps guessing; after each guess say *"Too high"* or *"Too low"*.
3. When correct, print *"🎉 You got it in N guesses!"*

**Bonus:**
- Limit the player to 7 guesses.
- Ask *"Play again? (y/n)"* at the end.
- Let the player choose a difficulty (easy 1–50, hard 1–500).

---

## ⚠️ Common mistakes
```python
if x = 5:        # ❌ SyntaxError: use == to compare
if x == 5:       # ✅
```
```python
if x > 5         # ❌ missing colon
    print(x)
```
- **IndentationError**: mixing tabs and spaces, or forgetting to indent after `:`.
- **Infinite loops**: forgetting to update the variable in a `while` loop. Press `Ctrl+C` to stop.
- `if day == "Sat" or "Sun":` ❌ is always True! Write `if day == "Sat" or day == "Sun":` ✅

## 🔗 Resources
- [Python docs: More Control Flow Tools](https://docs.python.org/3/tutorial/controlflow.html)
- [Real Python: Conditional Statements](https://realpython.com/python-conditional-statements/)
- [Real Python: for loops](https://realpython.com/python-for-loop/)

## ✅ Checklist
- [ ] I can write an `if/elif/else` chain
- [ ] I know the difference between `while` and `for`
- [ ] I can predict the output of `range(2, 10, 3)`
- [ ] I can explain `break` vs `continue`
- [ ] I built the guessing game
