from pathlib import Path

HERE = Path(__file__).parent
SAMPLE = HERE.parent / "exercises" / "sample.txt"


def file_stats(path):
    try:
        with open(path, encoding="utf-8") as f:
            text = f.read()
    except FileNotFoundError:
        print(f"Sorry, {path.name} doesn't exist.")
        return None
    return {
        "lines": len(text.splitlines()),
        "words": len(text.split()),
        "characters": len(text),
    }


stats = file_stats(SAMPLE)
print(stats)
assert stats == {"lines": 5, "words": 36, "characters": 218}
assert file_stats(HERE / "missing.txt") is None
print("✅ All checks passed!")
