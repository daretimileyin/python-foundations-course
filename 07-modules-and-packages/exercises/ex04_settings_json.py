"""
⭐⭐ Exercise 4 – Settings with JSON

Write a program that remembers user settings between runs.

1. load_settings(): read settings.json (next to this file) and return a dict.
   If the file doesn't exist, return the DEFAULTS.
2. save_settings(settings): write the dict to settings.json with indent=2.
3. main(): show the current settings, ask the user which setting to change
   and the new value, then save.

Run it twice and check your change was remembered!
"""
import json
from pathlib import Path

SETTINGS_FILE = Path(__file__).parent / "settings.json"
DEFAULTS = {"username": "guest", "theme": "light", "font_size": 14}

# Write your code here 👇
