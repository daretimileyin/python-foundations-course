"""Example 01 – Your first API request."""
import json

import requests

response = requests.get("https://api.github.com/users/octocat", timeout=10)

print("Status code:", response.status_code)
print("Content type:", response.headers.get("Content-Type"))

data = response.json()
print("\nThe first part of the JSON:")
print(json.dumps(data, indent=2)[:400], "...")

print("\nPicking out what we need:")
print(f"Name:         {data['name']}")
print(f"Public repos: {data['public_repos']}")
print(f"Followers:    {data['followers']}")
print(f"Profile:      {data['html_url']}")
