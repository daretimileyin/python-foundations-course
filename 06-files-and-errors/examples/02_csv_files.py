"""Example 02 – CSV files."""
import csv
from pathlib import Path

HERE = Path(__file__).parent
path = HERE / "example_people.csv"

people = [
    {"name": "Ada", "age": 36, "city": "London"},
    {"name": "Chinua", "age": 82, "city": "Ogidi"},
    {"name": "Grace", "age": 85, "city": "New York"},
]

with open(path, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "age", "city"])
    writer.writeheader()
    writer.writerows(people)
print(f"Wrote {len(people)} rows to {path.name}")

with open(path, newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    total_age = 0
    for row in reader:
        print(f"{row['name']:<8} {row['age']:>3}  {row['city']}")
        total_age += int(row["age"])   # CSV values are always strings!
print(f"Average age: {total_age / len(people):.1f}")

path.unlink()
