import requests

API = "https://api.dictionaryapi.dev/api/v2/entries/en/{}"


def lookup(word):
    """Return the list of entries for word, or None if not found / error."""
    try:
        response = requests.get(API.format(word), timeout=10)
    except requests.exceptions.Timeout:
        print("⏱️ Timed out.")
        return None
    except requests.exceptions.ConnectionError:
        print("📡 No connection.")
        return None
    if response.status_code == 404:
        print(f"🤷 '{word}' not found.")
        return None
    response.raise_for_status()
    return response.json()


def show(entries):
    for entry in entries:
        print(f"\n📖 {entry['word']}  {entry.get('phonetic', '')}")
        for meaning in entry["meanings"]:
            print(f"  [{meaning['partOfSpeech']}]")
            for d in meaning["definitions"][:2]:
                print(f"   • {d['definition']}")
                if d.get("example"):
                    print(f"     e.g. \"{d['example']}\"")


def main():
    while True:
        word = input("\nWord (or 'quit'): ").strip().lower()
        if word == "quit":
            break
        if word:
            entries = lookup(word)
            if entries:
                show(entries)


if __name__ == "__main__":
    main()
