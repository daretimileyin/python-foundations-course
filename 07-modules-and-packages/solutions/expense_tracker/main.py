"""Mini-project solution – Expense Tracker. Run: python3 main.py"""
from datetime import date

from storage import load_expenses, save_expenses


def add_expense(expenses):
    try:
        amount = float(input("Amount: "))
    except ValueError:
        print("Invalid amount.")
        return
    category = input("Category (food, transport, ...): ").strip().lower() or "other"
    description = input("Description: ").strip()
    expenses.append({
        "date": date.today().isoformat(),
        "amount": amount,
        "category": category,
        "description": description,
    })
    save_expenses(expenses)
    print("✅ Added.")


def list_expenses(expenses, month=None):
    shown = [e for e in expenses if month is None or e["date"].startswith(month)]
    if not shown:
        print("No expenses.")
    for e in shown:
        print(f"{e['date']}  {e['amount']:>9.2f}  {e['category']:<12} {e['description']}")


def show_totals(expenses):
    per_category = {}
    for e in expenses:
        per_category[e["category"]] = per_category.get(e["category"], 0) + e["amount"]
    print(f"TOTAL: {sum(per_category.values()):.2f}")
    for category, total in sorted(per_category.items(), key=lambda kv: kv[1], reverse=True):
        print(f"  {category:<12}{total:>9.2f}")
    if per_category:
        print("Biggest category:", max(per_category, key=per_category.get))


def main():
    expenses = load_expenses()
    while True:
        print("\n💰 EXPENSES\n1. Add\n2. List all\n3. Totals\n4. Filter by month\n5. Quit")
        choice = input("Choose: ").strip()
        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            list_expenses(expenses)
        elif choice == "3":
            show_totals(expenses)
        elif choice == "4":
            list_expenses(expenses, input("Month (YYYY-MM): ").strip())
        elif choice == "5":
            break


if __name__ == "__main__":
    main()
