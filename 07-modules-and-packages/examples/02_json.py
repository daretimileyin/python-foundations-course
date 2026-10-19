"""Example 02 – Saving and loading JSON."""
import json
from pathlib import Path

path = Path(__file__).parent / "example_library.json"

library = {
    "owner": "Ada",
    "books": [
        {"title": "Things Fall Apart", "author": "Chinua Achebe", "read": True},
        {"title": "Half of a Yellow Sun", "author": "Chimamanda Ngozi Adichie", "read": False},
    ],
}

with open(path, "w", encoding="utf-8") as f:
    json.dump(library, f, indent=2)
print("Saved. File contents:\n")
print(path.read_text(encoding="utf-8"))

with open(path, encoding="utf-8") as f:
    loaded = json.load(f)

loaded["books"].append({"title": "Purple Hibiscus", "author": "Chimamanda Ngozi Adichie", "read": False})
unread = [b["title"] for b in loaded["books"] if not b["read"]]
print("Unread books:", unread)

# Converting to/from a string (used a lot with web APIs)
as_text = json.dumps({"ok": True, "count": 3})
print("\nAs text:", as_text, type(as_text))
print("Back to dict:", json.loads(as_text))

path.unlink()
