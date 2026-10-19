"""Example 01 – Reading and writing text files."""
from pathlib import Path

HERE = Path(__file__).parent
notes = HERE / "example_notes.txt"

# Write (overwrites)
with open(notes, "w", encoding="utf-8") as f:
    f.write("Shopping list\n")
    f.write("- eggs\n")

# Append
with open(notes, "a", encoding="utf-8") as f:
    for item in ["bread", "milk", "plantain 🍌"]:
        f.write(f"- {item}\n")

# Read everything
with open(notes, encoding="utf-8") as f:
    print("Whole file:")
    print(f.read())

# Read line by line
with open(notes, encoding="utf-8") as f:
    for number, line in enumerate(f, start=1):
        print(f"{number}: {line.rstrip()}")

# pathlib shortcuts
print("\nExists?", notes.exists())
print("Name:", notes.name, "| Suffix:", notes.suffix)
print("Line count:", len(notes.read_text(encoding="utf-8").splitlines()))

notes.unlink()   # delete the file so the repo stays clean
print("Deleted example file.")
