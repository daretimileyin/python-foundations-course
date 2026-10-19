# Module 09 – Testing & Debugging

## 🎯 Learning objectives
By the end of this module you will be able to:
- Read tracebacks confidently and find the line that broke
- Debug with `print`, the VS Code debugger and `breakpoint()`
- Write automated tests with **pytest**
- Test that code raises the right errors
- Use fixtures and parametrised tests
- Think about **edge cases**
- Follow a simple test-driven development (TDD) workflow

> Install pytest first (inside your activated venv): `pip install pytest`

---

## 📖 Concepts

### 1. Types of errors
| Kind | Example | When you find out |
|------|---------|-------------------|
| **Syntax error** | missing `:` or `)` | Before the program runs |
| **Runtime error** (exception) | `ZeroDivisionError` | While running |
| **Logic error** (bug) | using `>` instead of `>=` | Only when the output is wrong 😬 |

Tests are how we catch **logic errors**.

### 2. Debugging strategies
1. **Read the error message** (bottom line first) and go to the line number.
2. **Reproduce** the problem reliably.
3. **Print debugging**: `print(f"{x=}")` prints `x=42`, very handy.
4. **Rubber duck**: explain your code line by line out loud. You'll often spot the bug yourself.
5. **Divide and conquer**: comment out half the code to find where the problem starts.
6. **Check your assumptions**: is that variable *really* what you think it is? Print its `type()`.

### 3. The VS Code debugger
1. Click in the margin left of a line number to set a **breakpoint** (red dot).
2. Press **F5** → *Python File*.
3. The program pauses at the breakpoint. Now you can:
   - hover over variables to see their values
   - **F10** step over (next line)
   - **F11** step into a function
   - **F5** continue
   - use the *Debug Console* to run expressions
You can also put `breakpoint()` in your code to pause there in the terminal (type `n` next, `p x` print, `c` continue, `q` quit).

### 4. Why automated tests?
`assert` checks at the bottom of a file (like in Modules 04–08) are a start. **pytest** makes tests organised, repeatable and informative.

### 5. Your first pytest test
```python
# calculator.py
def add(a, b):
    return a + b
```
```python
# test_calculator.py
from calculator import add

def test_add_positive_numbers():
    assert add(2, 3) == 5

def test_add_negative_numbers():
    assert add(-1, -1) == -2
```
Run:
```bash
pytest                 # finds files named test_*.py and functions named test_*
pytest -v              # verbose: shows each test
pytest path/to/test_file.py
```

### 6. Testing for errors
```python
import pytest

def test_divide_by_zero_raises():
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)

def test_error_message():
    with pytest.raises(ValueError, match="positive"):
        withdraw(100, -5)
```

### 7. Comparing floats
```python
assert 0.1 + 0.2 == 0.3                    # ❌ fails! (floating point)
assert 0.1 + 0.2 == pytest.approx(0.3)     # ✅
```

### 8. Parametrised tests: many cases, one test
```python
@pytest.mark.parametrize("n, expected", [
    (2, True),
    (3, True),
    (4, False),
    (1, False),
    (0, False),
])
def test_is_prime(n, expected):
    assert is_prime(n) == expected
```

### 9. Fixtures: reusable setup
```python
@pytest.fixture
def account():
    return BankAccount("Ada", balance=100)

def test_deposit(account):
    account.deposit(50)
    assert account.balance == 150
```

### 10. Edge cases: where bugs hide
Always ask: what about…
- empty input (`""`, `[]`)
- zero, negative numbers, very large numbers
- one item vs many
- wrong types
- boundaries (exactly 60 for a pass mark of 60)

### 11. TDD (Test-Driven Development)
1. 🔴 **Red**: write a test for a feature that doesn't exist yet, and watch it fail
2. 🟢 **Green**: write the simplest code to make it pass
3. 🔵 **Refactor**: clean up the code, and keep the tests green

---

## 🧪 Examples
| File | Shows |
|------|-------|
| [`calculator.py`](examples/calculator.py) | Code under test |
| [`test_calculator.py`](examples/test_calculator.py) | Basic tests, `raises`, `approx`, parametrize, fixture |
| [`buggy_code.py`](examples/buggy_code.py) | Practise with the debugger: find the bugs! |

Run the example tests:
```bash
pytest 09-testing-and-debugging/examples -v
```

---

## ✍️ Exercises
| # | File | Difficulty | Task |
|---|------|-----------|------|
| 1 | `ex01_fix_the_bugs.py` | ⭐ | Find and fix 4 bugs using the debugger |
| 2 | `text_utils.py` + `test_text_utils.py` | ⭐⭐ | Write tests for existing functions |
| 3 | `test_bank.py` | ⭐⭐ | Test your Module 08 bank account (fixtures!) |
| 4 | `ex04_tdd_fizzbuzz/` | ⭐⭐⭐ | Build a function test-first |

---

## 🛠️ Mini-project: Test Your Old Projects
Pick **two** of your previous mini-projects (e.g. unit converter, word counter, contact book).
1. Refactor them so the logic lives in functions or classes that **return** values (instead of only printing) and the `input()`/`print()` lives in `main()`.
2. Write a `test_<project>.py` with **at least 8 tests** each, including edge cases.
3. Get every test passing: `pytest -v`.

This is a really important skill: **separating logic from input/output makes code testable.**

---

## ⚠️ Common mistakes
- Test file or function not starting with `test_` means pytest won't find it.
- Testing functions that `print` instead of `return`; you can't easily assert on printed output.
- Tests that depend on each other or run in a certain order. Each test should stand alone.
- Only testing the "happy path". Test the edge cases too!
- `ModuleNotFoundError` when importing: run pytest from the repo root, or check the import path.

## 🔗 Resources
- [pytest: Getting Started](https://docs.pytest.org/en/stable/getting-started.html)
- [Real Python: Effective Testing with pytest](https://realpython.com/pytest-python-testing/)
- [VS Code: Python Debugging](https://code.visualstudio.com/docs/python/debugging)
- [Real Python: Python Debugging with pdb](https://realpython.com/python-debugging-pdb/)

## ✅ Checklist
- [ ] I can use breakpoints and step through code in VS Code
- [ ] I can write and run pytest tests
- [ ] I can test that an error is raised
- [ ] I can write a parametrised test and a fixture
- [ ] I think about edge cases when testing
- [ ] My old projects have passing tests
