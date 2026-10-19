# 🔁 Workflow: How to Submit Your Work

We work like a real software team: **you never push directly to `main`.** Each module is done on its own branch and submitted as a Pull Request (PR) for review.

---

## The cycle (repeat for every module)

### 1. Get the latest version of `main`
```bash
git checkout main
git pull
```

### 2. Create a branch for the module
```bash
git checkout -b module-01-basics
```
Branch naming: `module-XX-short-name` (e.g. `module-03-data-structures`).

### 3. Do the work
- Read the module `README.md`.
- Run and play with the files in `examples/`.
- Complete the files in `exercises/`.
- Build the mini-project.

### 4. Commit as you go (small, frequent commits)
```bash
git status                     # see what changed
git add 01-basics/exercises/ex01_greeting.py
git commit -m "Complete exercise 1: greeting"
```

**Good commit messages** say *what* you did:
- ✅ `Add temperature converter exercise`
- ✅ `Fix off-by-one error in loop`
- ❌ `stuff`
- ❌ `asdfgh`

### 5. Push your branch
```bash
git push -u origin module-01-basics
```

### 6. Open a Pull Request
- On GitHub you'll see a yellow banner, **"Compare & pull request"**. Click it.
- Or with the GitHub CLI: `gh pr create --fill`
- Fill in the PR template (it appears automatically).
- Request a review from your mentor.

### 7. Respond to review
- Read every comment. Ask if something is unclear!
- Make changes on the **same branch**, commit and push again. The PR updates automatically.

### 8. Merge 🎉
Once approved, the PR is merged into `main`. Tick the module off in `PROGRESS.md`, then start again from step 1 with the next module.

---

## Asking questions

Open an **Issue** (Issues tab → *New issue* → *Question*). Include:
- Which module/exercise
- What you're trying to do
- Your code (in a code block)
- The full error message
- What you've already tried

### How to format code in GitHub

````markdown
```python
print("hello")
```
````

---

## Useful Git commands cheat sheet

| Command | What it does |
|---------|--------------|
| `git status` | Show changed files |
| `git diff` | Show exactly what changed |
| `git add <file>` | Stage a file for commit |
| `git add .` | Stage everything (be careful!) |
| `git commit -m "msg"` | Save a snapshot |
| `git log --oneline` | Show history |
| `git branch` | List branches |
| `git checkout <branch>` | Switch branch |
| `git checkout -b <name>` | Create and switch to a new branch |
| `git pull` | Download latest changes |
| `git push` | Upload your commits |
| `git restore <file>` | Undo uncommitted changes to a file |
