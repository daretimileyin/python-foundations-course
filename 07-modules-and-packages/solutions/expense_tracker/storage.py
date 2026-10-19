import json
from pathlib import Path

DATA_FILE = Path(__file__).parent / "expenses.json"


def load_expenses():
    try:
        with open(DATA_FILE, encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def save_expenses(expenses):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(expenses, f, indent=2)
