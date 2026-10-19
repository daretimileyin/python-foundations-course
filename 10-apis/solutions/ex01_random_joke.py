import requests

URL = "https://official-joke-api.appspot.com/random_joke"

while True:
    try:
        joke = requests.get(URL, timeout=10).json()
    except requests.exceptions.RequestException:
        print("Couldn't fetch a joke right now.")
        break
    print("\n" + joke["setup"])
    input("(press Enter)")
    print(joke["punchline"], "😂")
    if input("\nAnother one? (y/n) ").lower() != "y":
        break
