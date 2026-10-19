shopping = []

while True:
    command = input("Command (add/remove/show/quit): ").strip().lower()
    if command == "add":
        item = input("Item: ")
        shopping.append(item)
    elif command == "remove":
        item = input("Item: ")
        if item in shopping:
            shopping.remove(item)
        else:
            print(f"{item} is not on the list.")
    elif command == "show":
        if not shopping:
            print("The list is empty.")
        for i, item in enumerate(shopping, start=1):
            print(f"{i}. {item}")
    elif command == "quit":
        break
    else:
        print("Unknown command.")
