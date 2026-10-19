import csv
from pathlib import Path

EXERCISES = Path(__file__).parent.parent / "exercises"
SUBJECTS = ["maths", "english", "science"]

with open(EXERCISES / "grades.csv", newline="", encoding="utf-8") as f:
    students = list(csv.DictReader(f))

report_rows = []
for s in students:
    average = sum(int(s[subject]) for subject in SUBJECTS) / len(SUBJECTS)
    report_rows.append({
        "name": s["name"],
        "average": round(average, 1),
        "result": "PASS" if average >= 60 else "FAIL",
    })

report_path = Path(__file__).parent / "report.csv"
with open(report_path, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "average", "result"])
    writer.writeheader()
    writer.writerows(report_rows)
print(f"Report written to {report_path.name}")

for subject in SUBJECTS:
    best = max(students, key=lambda s: int(s[subject]))
    print(f"Best in {subject}: {best['name']} ({best[subject]})")
