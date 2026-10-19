# 🛠️ Setup Guide

Do this once before starting Module 00. It takes about 30–60 minutes.

---

## 1. Install Python (3.11 or newer)

### Windows
1. Go to <https://www.python.org/downloads/> and download the latest version.
2. Run the installer. **IMPORTANT:** tick ✅ **"Add python.exe to PATH"** at the bottom of the first screen.
3. Click *Install Now*.

### macOS
Download the installer from <https://www.python.org/downloads/>, or with [Homebrew](https://brew.sh):
```bash
brew install python
```

### Linux
Python is usually pre-installed. Otherwise:
```bash
sudo apt install python3 python3-pip python3-venv
```

### ✅ Check it worked
Open a terminal (Windows: *PowerShell*; macOS: *Terminal*) and run:
```bash
python3 --version     # macOS / Linux
python --version      # Windows
```
You should see something like `Python 3.12.4`.

---

## 2. Install VS Code

1. Download from <https://code.visualstudio.com/>.
2. Open VS Code → Extensions (square icon on the left) → install:
   - **Python** (by Microsoft)
   - **Pylance** (usually installed with Python)
3. Optional but nice: **Error Lens** (shows errors inline).

---

## 3. Install Git

- **Windows:** <https://git-scm.com/download/win> (default options are fine)
- **macOS:** run `git --version`; if not installed, macOS will offer to install it.
- **Linux:** `sudo apt install git`

Configure your identity (use the same email as your GitHub account):
```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
git config --global init.defaultBranch main
```

---

## 4. Create a GitHub account & accept the invite

1. Sign up at <https://github.com>.
2. Accept the collaborator invitation sent to your email (or check <https://github.com/notifications>).
3. Install the GitHub CLI (optional, makes life easier): <https://cli.github.com/>, then run `gh auth login`.

---

## 5. Clone this repository

```bash
cd ~/Documents          # or wherever you keep projects
git clone https://github.com/<OWNER>/<REPO>.git
cd <REPO>
code .                  # opens the folder in VS Code
```

---

## 6. Create a virtual environment (recommended)

A virtual environment keeps this project's packages separate from the rest of your computer.

```bash
# create it (once)
python3 -m venv .venv

# activate it (every time you open a new terminal)
source .venv/bin/activate          # macOS / Linux
.venv\Scripts\Activate.ps1         # Windows PowerShell

# install packages used later in the course
pip install -r requirements.txt
```

When activated, you'll see `(.venv)` at the start of your terminal prompt.

> 💡 In VS Code press `Ctrl+Shift+P` (`Cmd+Shift+P` on Mac) → *Python: Select Interpreter* → choose the `.venv` one.

---

## ✅ Setup checklist

- [ ] `python3 --version` (or `python --version`) prints 3.11+
- [ ] VS Code installed with the Python extension
- [ ] `git --version` works and `user.name`/`user.email` are set
- [ ] Repository cloned and opened in VS Code
- [ ] Virtual environment created and activated

All done? Head to [00-setup](00-setup/README.md). 🎉
