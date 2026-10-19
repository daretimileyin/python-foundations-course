# ⭐⭐ To-Do List CLI
**Do this after:** Module 06 (better still, after Module 07)

## Requirements
- Commands: `add <task>`, `list`, `done <number>`, `delete <number>`, `quit`
- Each task has a title and done/not-done status
- Tasks are **saved to a file** and loaded when the program starts
- Bad input never crashes the program (e.g. `done abc`, `delete 99`)

Example:
```
> add Learn about APIs
Added: Learn about APIs
> list
1. [ ] Learn about APIs
2. [x] Finish Module 06
> done 1
```

## Stretch goals
- Priorities (high/medium/low) and sort by priority
- Due dates; highlight overdue tasks
- Use `argparse` so it works like `python3 todo.py add "Buy milk"`
