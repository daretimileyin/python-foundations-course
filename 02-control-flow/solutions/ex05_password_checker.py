PASSWORD = "python123"
MAX_ATTEMPTS = 3

attempts = 0
while attempts < MAX_ATTEMPTS:
    guess = input("Password: ")
    attempts += 1
    if guess == PASSWORD:
        print("Access granted ✅")
        break
    remaining = MAX_ATTEMPTS - attempts
    if remaining > 0:
        print(f"Wrong password. {remaining} attempts left.")
else:
    # A while loop's else runs only if the loop ended WITHOUT break
    print("Account locked 🔒")
