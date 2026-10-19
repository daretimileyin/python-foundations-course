# Module 07 – Modules, Packages & the Standard Library

## 🎯 Learning objectives
By the end of this module you will be able to:
- Import modules in different ways
- Use popular standard-library modules: `random`, `math`, `datetime`, `os`, `json`, `collections`
- Split your own code across multiple files
- Understand `if __name__ == "__main__":`
- Create a virtual environment and install packages with `pip`
- Save and load data as JSON

---

## 📖 Concepts

### 1. What is a module?
A **module** is just a `.py` file. A **package** is a folder of modules (often with an `__init__.py`). Python comes with hundreds of modules, the **standard library** ("batteries included").

### 2. Ways to import
```python
import math
math.sqrt(16)                  # 4.0

from math import sqrt, pi
sqrt(16)                       # no "math." needed

import datetime as dt          # alias
dt.date.today()

from random import *           # ❌ avoid: you can't tell where names come from
```

### 3. Standard library tour
```python
import random
random.randint(1, 6)                 # dice roll
random.choice(["rock", "paper", "scissors"])
random.shuffle(my_list)

import math
math.ceil(4.2), math.floor(4.8), math.pi, math.factorial(5)

from datetime import datetime, date, timedelta
now = datetime.now()
now.strftime("%d/%m/%Y %H:%M")       # '19/10/2026 14:30'
date.today() + timedelta(days=7)     # a week from today

import os
os.getcwd()                          # current folder
os.environ.get("HOME")               # environment variable

from collections import Counter
Counter("mississippi").most_common(2)  # [('i', 4), ('s', 4)]
```

### 4. JSON: saving structured data
JSON looks just like Python dicts/lists and is the most common data format on the web.
```python
import json

data = {"name": "Ada", "skills": ["maths", "poetry"]}

with open("data.json", "w") as f:
    json.dump(data, f, indent=2)       # save

with open("data.json") as f:
    loaded = json.load(f)              # load

text = json.dumps(data)                # dict → string
back = json.loads(text)                # string → dict
```

### 5. Your own modules
```
my_project/
├── main.py
└── helpers.py
```
```python
# helpers.py
def shout(text):
    return text.upper() + "!"
```
```python
# main.py
from helpers import shout
print(shout("hello"))
```

### 6. `if __name__ == "__main__":`
When Python runs a file directly, it sets `__name__` to `"__main__"`. When the file is **imported**, `__name__` is the module's name.
```python
def main():
    ...

if __name__ == "__main__":
    main()        # runs only when executed directly, NOT on import
```

### 7. Packages
```
my_package/
├── __init__.py      # marks the folder as a package (can be empty)
├── geometry.py
└── text_tools.py
```
```python
from my_package.geometry import circle_area
```

### 8. pip and virtual environments
```bash
python3 -m venv .venv               # create
source .venv/bin/activate           # activate (Windows: .venv\Scripts\Activate.ps1)
pip install requests                # install a package from PyPI
pip list                            # what's installed
pip freeze > requirements.txt       # save the list
pip install -r requirements.txt     # install from the list
deactivate                          # leave the venv
```
Find packages at <https://pypi.org>.

---

## 🧪 Examples
| File | Shows |
|------|-------|
| [`01_standard_library.py`](examples/01_standard_library.py) | random, math, datetime, Counter |
| [`02_json.py`](examples/02_json.py) | Saving and loading JSON |
| [`03_using_my_package.py`](examples/03_using_my_package.py) + [`my_package/`](examples/my_package/) | Importing your own package |

---

## ✍️ Exercises
| # | File | Difficulty | Task |
|---|------|-----------|------|
| 1 | `ex01_dice_and_dates.py` | ⭐ | Use `random` and `datetime` |
| 2 | `ex02_password_generator.py` | ⭐⭐ | Generate random passwords with `random` and `string` |
| 3 | `ex03_my_module/` | ⭐⭐ | Move functions into your own module and import them |
| 4 | `ex04_settings_json.py` | ⭐⭐ | Save and load user settings as JSON |

---

## 🛠️ Mini-project: Expense Tracker
Create `exercises/expense_tracker/` with **two files**:
- `storage.py`: `load_expenses()` and `save_expenses(expenses)` using JSON in `expenses.json`
- `main.py`: the menu program:
  1. Add expense (amount, category, description; date added automatically)
  2. List all expenses
  3. Show total spent, and total per category
  4. Quit (data is saved so it's still there next time!)

**Bonus:** filter expenses by month; show the biggest category with `Counter` or `max`.

---

## ⚠️ Common mistakes
- **Naming your file the same as a module**: a file called `random.py` or `json.py` breaks `import random`/`import json`!
- `ModuleNotFoundError: No module named 'requests'`: install it, and check your venv is activated.
- Forgetting `indent=2` makes JSON files hard to read.
- JSON keys are always strings: `{1: "a"}` comes back as `{"1": "a"}`.

## 🔗 Resources
- [Python docs: Modules](https://docs.python.org/3/tutorial/modules.html)
- [Python Standard Library index](https://docs.python.org/3/library/index.html)
- [Real Python: Virtual Environments](https://realpython.com/python-virtual-environments-a-primer/)
- [Real Python: Working with JSON](https://realpython.com/python-json/)

## ✅ Checklist
- [ ] I can import a module three different ways
- [ ] I know what `if __name__ == "__main__":` does
- [ ] I split code across multiple files
- [ ] I can create a venv and `pip install` a package
- [ ] I can save and load JSON
- [ ] I built the expense tracker
