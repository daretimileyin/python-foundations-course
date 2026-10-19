"""Mini-project solution – Contact Book."""

contacts = {}

while True:
    print("\n📒 CONTACT BOOK")
    print("1. Add contact\n2. View all\n3. Search\n4. Delete\n5. Quit")
    choice = input("Choose: ").strip()

    if choice == "1":
        name = input("Name: ").strip()
        phone = input("Phone: ").strip()
        email = input("Email: ").strip()
        contacts[name] = {"phone": phone, "email": email}
        print(f"✅ {name} saved.")

    elif choice == "2":
        if not contacts:
            print("No contacts yet.")
        for name in sorted(contacts):
            info = contacts[name]
            print(f"- {name}: {info['phone']} | {info['email']}")

    elif choice == "3":
        query = input("Search for: ").strip().lower()
        matches = [n for n in contacts if query in n.lower()]
        if not matches:
            print("No matches.")
        for name in matches:
            print(f"- {name}: {contacts[name]['phone']} | {contacts[name]['email']}")

    elif choice == "4":
        name = input("Name to delete: ").strip()
        if name in contacts:
            del contacts[name]
            print(f"🗑️ {name} deleted.")
        else:
            print("Contact not found.")

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Please choose 1-5.")
