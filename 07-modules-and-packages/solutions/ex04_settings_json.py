import json
from pathlib import Path

SETTINGS_FILE = Path(__file__).parent / "settings.json"
DEFAULTS = {"username": "guest", "theme": "light", "font_size": 14}


def load_settings():
    try:
        with open(SETTINGS_FILE, encoding="utf-8") as f:
            return {**DEFAULTS, **json.load(f)}
    except FileNotFoundError:
        return DEFAULTS.copy()


def save_settings(settings):
    with open(SETTINGS_FILE, "w", encoding="utf-8") as f:
        json.dump(settings, f, indent=2)


def main():
    settings = load_settings()
    print("Current settings:")
    for key, value in settings.items():
        print(f"  {key}: {value}")

    key = input("Setting to change (blank to skip): ").strip()
    if key not in settings:
        print("No changes made.")
        return
    value = input(f"New value for {key}: ").strip()
    if isinstance(DEFAULTS[key], int):
        value = int(value)
    settings[key] = value
    save_settings(settings)
    print("✅ Saved!")


if __name__ == "__main__":
    main()
