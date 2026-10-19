"""
⭐⭐⭐ Exercise 4 – Command-line Dictionary

Build a dictionary app with the Free Dictionary API:
    https://api.dictionaryapi.dev/api/v2/entries/en/<word>

Requirements:
  - Loop: ask for a word until the user types 'quit'
  - Show each part of speech (noun, verb...) with up to 2 definitions
    and an example if one exists
  - Handle unknown words (404), timeouts and connection errors
  - Put the API call in its own function: lookup(word) -> list | None
"""
import requests

# Write your code here 👇
