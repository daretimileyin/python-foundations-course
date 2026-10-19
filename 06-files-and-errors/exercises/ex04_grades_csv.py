"""
⭐⭐ Exercise 4 – Grades CSV

1. Read grades.csv (in this folder) using csv.DictReader.
2. For each student calculate their average across the three subjects.
3. Write a new file report.csv with columns:
       name,average,result
   where result is "PASS" if average >= 60 else "FAIL"
   (average rounded to 1 decimal place)
4. Print the name of the best student in each subject.
"""
import csv
from pathlib import Path

HERE = Path(__file__).parent

# Write your code here 👇
