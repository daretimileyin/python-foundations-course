"""
⭐⭐ Exercise 3 – File Stats

Write file_stats(path) that returns a dictionary:
    {"lines": ..., "words": ..., "characters": ...}

Use the sample.txt file in this folder.
If the file doesn't exist, print a friendly message and return None.

Hint: build the path with  Path(__file__).parent / "sample.txt"
"""
from pathlib import Path

HERE = Path(__file__).parent


def file_stats(path):
    # TODO
    pass


stats = file_stats(HERE / "sample.txt")
print(stats)
assert stats == {"lines": 5, "words": 36, "characters": 218}
assert file_stats(HERE / "missing.txt") is None
print("✅ All checks passed!")
