"""Mini-project solution – Personal Journal."""
from datetime import datetime
from pathlib import Path

JOURNAL = Path(__file__).parent / "journal.txt"
SEPARATOR = "-" * 40


def write_entry():
    text = input("What's on your mind?\n> ").strip()
    if not text:
        print("Empty entry not saved.")
        return
    stamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    with open(JOURNAL, "a", encoding="utf-8") as f:
        f.write(f"[{stamp}]\n{text}\n{SEPARATOR}\n")
    print("✅ Saved.")


def read_entries():
    try:
        return JOURNAL.read_text(encoding="utf-8").split(SEPARATOR + "\n")
    except FileNotFoundError:
        return []


def show_all():
    entries = [e for e in read_entries() if e.strip()]
    if not entries:
        print("Your journal is empty.")
    for entry in entries:
        print(entry.strip(), end="\n\n")
    print(f"({len(entries)} entries)")


def search():
    word = input("Search for: ").lower()
    matches = [e for e in read_entries() if word in e.lower()]
    print(f"Found {len(matches)} entr{'y' if len(matches) == 1 else 'ies'}.")
    for entry in matches:
        print(entry.strip(), end="\n\n")


def delete_all():
    if input("Delete EVERYTHING? Type 'yes' to confirm: ") == "yes":
        JOURNAL.unlink(missing_ok=True)
        print("🗑️ Journal deleted.")


def main():
    actions = {"1": write_entry, "2": show_all, "3": search, "4": delete_all}
    while True:
        print("\n📔 JOURNAL\n1. Write entry\n2. Read all\n3. Search\n4. Delete all\n5. Quit")
        choice = input("Choose: ").strip()
        if choice == "5":
            break
        action = actions.get(choice)
        if action:
            action()
        else:
            print("Please choose 1-5.")


if __name__ == "__main__":
    main()
