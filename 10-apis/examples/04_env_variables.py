"""Example 04 – Loading secrets from a .env file.

1. Copy .env.example to .env in this folder
2. Put any value in MY_API_KEY
3. Run this file
"""
import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv(Path(__file__).parent / ".env")

api_key = os.getenv("MY_API_KEY")

if not api_key or api_key == "replace-me":
    print("⚠️ MY_API_KEY is not set. Copy .env.example to .env and fill it in.")
else:
    # Never print a full key! Show just enough to confirm it loaded.
    print(f"✅ Key loaded: {api_key[:3]}{'*' * (len(api_key) - 3)}")
    # You'd then use it like:
    # requests.get(url, headers={"Authorization": f"Bearer {api_key}"}, timeout=10)
