students = {
    "Ada": [90, 85, 85],
    "Bob": [50, 60, 55],
    "Chioma": [70, 95, 88],
    "David": [40, 65, 72],
}

averages = {}
for name, grades in students.items():
    avg = sum(grades) / len(grades)
    averages[name] = avg
    status = "PASS" if avg >= 60 else "FAIL"
    print(f"{name}: {avg:.1f} – {status}")

best = max(averages, key=averages.get)
print(f"\nTop student: {best} ({averages[best]:.1f})")
