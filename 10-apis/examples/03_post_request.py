"""Example 03 – Sending data with POST (to a fake practice API)."""
import requests

new_post = {
    "title": "Learning Python",
    "body": "Today I learned how to make POST requests!",
    "userId": 1,
}

response = requests.post("https://jsonplaceholder.typicode.com/posts", json=new_post, timeout=10)
print("Status:", response.status_code)    # 201 = Created
print("Server replied:", response.json())

# GET with filtering
response = requests.get(
    "https://jsonplaceholder.typicode.com/posts", params={"userId": 1}, timeout=10
)
posts = response.json()
print(f"\nUser 1 has {len(posts)} posts. First three titles:")
for post in posts[:3]:
    print(" -", post["title"])
