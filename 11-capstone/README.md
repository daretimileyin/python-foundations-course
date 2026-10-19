# Module 11 – Capstone Project 🎓

## 🎯 Goal
Plan, build, test and present **your own project** using everything you've learned. This is the project you show people when they ask "what can you build?"

---

## 📋 Requirements
Your project must:
- [ ] Solve a real problem or be genuinely fun to use
- [ ] Be split into **multiple files/modules**
- [ ] Use **at least one class**
- [ ] **Save data** (JSON, CSV, or a SQLite database)
- [ ] **Handle errors** gracefully (no crashes on bad input)
- [ ] Have **at least 10 pytest tests**
- [ ] Have its own **README.md** (see the template below)
- [ ] Have a clean Git history with meaningful commits
- [ ] Optional: use an API or an external package

---

## 💡 Project ideas
| Idea | Skills it stretches |
|------|---------------------|
| 📚 **Study planner**: subjects, deadlines, reminders, progress | Classes, dates, JSON |
| 💸 **Personal finance tracker**: income/expenses, monthly reports, CSV export | Files, data analysis |
| 🎮 **Text adventure game**: rooms, inventory, saving progress | OOP, game state |
| 🌦️ **Weather + clothing advisor**: what should I wear today? | APIs, logic |
| 🏋️ **Workout logger**: exercises, sets, personal bests, charts | Data, `matplotlib` |
| 📰 **News headline reader**: from a news API, with saved favourites | APIs, JSON |
| 🔗 **URL shortener / link saver** with tags and search | Data structures, files |
| 🧠 **Flashcard quiz** with spaced repetition | Algorithms, dates |
| 🌐 **Simple web app** with Flask (stretch goal!) | New framework |
| 🤖 **Telegram/Discord bot** | APIs, async (stretch goal!) |

Have your own idea? Even better! Discuss it with your mentor first.

---

## 🗓️ Suggested timeline (3–4 weeks)

### Week 1: Plan
1. Open a GitHub **Issue** titled `Capstone proposal: <name>` describing:
   - What problem it solves and who it's for
   - The main features (must-have vs nice-to-have)
   - What data you'll store
   - A rough sketch of the classes/files
2. Agree the scope with your mentor. **Start small**; you can always add more.

### Week 2: Build the core
- Create `11-capstone/<your-project-name>/`
- Build the must-have features first
- Commit after each small working step
- Open a **draft Pull Request** early so your mentor can follow along

### Week 3: Polish
- Error handling and input validation
- Tests (aim for the important logic, not `input()`/`print()`)
- Nice-to-have features if time allows

### Week 4: Ship
- Write the README
- Final review and merge
- **Demo it** to your mentor (and anyone else who'll listen!) 🎉

---

## 📁 Suggested structure
```
11-capstone/my-project/
├── README.md
├── requirements.txt       # if you use external packages
├── main.py                # entry point: menus, input/output
├── models.py              # your classes
├── storage.py             # load/save data
├── utils.py               # helper functions
└── tests/
    ├── conftest.py
    ├── test_models.py
    └── test_storage.py
```

---

## 📝 Project README template
```markdown
# Project Name

One sentence describing what it does.

## Features
- ...

## Screenshots / Demo
(paste terminal output or a GIF)

## How to run
pip install -r requirements.txt
python3 main.py

## How to test
pytest -v

## What I learned
- ...

## Future ideas
- ...
```

---

## 🏆 Assessment rubric
| Area | 🌱 Getting there | 🌿 Good | 🌳 Excellent |
|------|------------------|---------|--------------|
| **Functionality** | Core feature works | All must-haves work | Polished, extras included |
| **Code quality** | Works but messy | Clear names, functions | Well-organised modules, DRY, docstrings |
| **Error handling** | Crashes on bad input | Handles common errors | Handles edge cases gracefully |
| **Testing** | A few tests | 10+ meaningful tests | Edge cases, fixtures, parametrize |
| **Git & docs** | Few big commits | Regular commits, README | Clean history, great README |

---

## 🎉 What's next after this course?
- **Web development:** Flask or Django, FastAPI
- **Data science:** pandas, matplotlib, Jupyter notebooks
- **Automation:** scripting your daily tasks, web scraping with BeautifulSoup
- **Practice problems:** [Exercism](https://exercism.org/tracks/python), [Advent of Code](https://adventofcode.com), [LeetCode](https://leetcode.com)
- **Books:** *Automate the Boring Stuff with Python* (free online), *Python Crash Course*

Congratulations on getting here! 🐍💪
