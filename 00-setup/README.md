# Module 00 – Setup & Your First Program

## 🎯 Learning objectives
By the end of this module you will be able to:
- Open a terminal and move between folders
- Run a Python file and use the interactive Python shell (REPL)
- Make your first commit, push a branch and open a Pull Request

> ⚠️ Finish [SETUP.md](../SETUP.md) before starting this module.

---

## 📖 Concepts

### 1. The terminal
The terminal is a text-based way to talk to your computer. You'll use it constantly.

| Command (macOS/Linux) | Windows PowerShell | What it does |
|-----------------------|--------------------|--------------|
| `pwd` | `pwd` | Print the folder you're in |
| `ls` | `ls` / `dir` | List files |
| `cd folder` | `cd folder` | Go into a folder |
| `cd ..` | `cd ..` | Go up one folder |
| `mkdir name` | `mkdir name` | Make a folder |
| `clear` | `cls` | Clear the screen |

💡 Press **Tab** to auto-complete file names. Press **↑** to repeat previous commands.

### 2. The Python REPL
Type `python3` (or `python` on Windows) in the terminal:
```
>>> 2 + 3
5
>>> print("Hello!")
Hello!
>>> exit()
```
REPL = **R**ead **E**valuate **P**rint **L**oop. It's great for quick experiments.

### 3. Running a Python file
Python files end in `.py`. To run one:
```bash
python3 path/to/file.py
```
In VS Code you can also click the ▶️ button in the top right.

### 4. What is Git? What is GitHub?
- **Git** is a tool on your computer that records snapshots (*commits*) of your code, so you can always go back.
- **GitHub** is a website that stores Git repositories online so people can collaborate.
- A **branch** is a separate line of work. You do your work on a branch, then ask for it to be merged into `main` with a **Pull Request**.

---

## ✍️ Exercises

### ⭐ Exercise 1: Explore the terminal
In your terminal, navigate into this repository, list its files, then go into `00-setup` and back out again.

### ⭐ Exercise 2: Use the REPL as a calculator
Open the REPL and calculate:
1. `365 * 24` (hours in a year)
2. `2 ** 10` (what does `**` do?)
3. `17 / 5` and `17 // 5` and `17 % 5`. What's the difference?

Write your answers as comments in `exercises/about_me.py`.

### ⭐ Exercise 3: Your first program
Open [`exercises/about_me.py`](exercises/about_me.py) and follow the instructions inside. Run it with:
```bash
python3 00-setup/exercises/about_me.py
```

---

## 🛠️ Mini-project: Hello GitHub
Submit your first Pull Request:
1. `git checkout -b module-00-setup`
2. Complete `exercises/about_me.py`
3. Tick Module 00 in `PROGRESS.md`
4. `git add .` → `git commit -m "Complete module 00"` → `git push -u origin module-00-setup`
5. Open a Pull Request on GitHub and request a review.

Full details in [CONTRIBUTING.md](../CONTRIBUTING.md).

---

## ⚠️ Common mistakes
- **`python: command not found`**: try `python3`; on Windows, reinstall Python and tick *Add to PATH*.
- **`No such file or directory`**: you're in the wrong folder. Use `pwd` and `ls` to check where you are.
- **Typing Python code into the terminal instead of the REPL**: if you see `>>>` you're in Python; if not, you're in the terminal.
- **Forgetting to save the file** before running it (VS Code shows a ● on unsaved tabs).

## 🔗 Resources
- [Official Python tutorial](https://docs.python.org/3/tutorial/)
- [GitHub's Git Handbook](https://docs.github.com/en/get-started/using-git/about-git)
- [Learn Git Branching (interactive game)](https://learngitbranching.js.org/)

## ✅ Checklist
- [ ] I can navigate folders in the terminal
- [ ] I can start and exit the Python REPL
- [ ] I can run a `.py` file
- [ ] I opened my first Pull Request
