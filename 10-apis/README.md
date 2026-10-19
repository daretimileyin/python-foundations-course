# Module 10 – Working with APIs

## 🎯 Learning objectives
By the end of this module you will be able to:
- Explain what an API is and how HTTP requests work
- Make `GET` and `POST` requests with the `requests` library
- Read JSON responses and pull out the data you need
- Use query parameters and headers
- Handle network errors and bad status codes
- Keep API keys secret with environment variables and `.env` files

> Install packages first (inside your venv): `pip install requests python-dotenv`

---

## 📖 Concepts

### 1. What is an API?
An **API** (Application Programming Interface) lets programs talk to each other. A **web API** is a URL you send a request to, and it replies with data (usually JSON).

Think of a restaurant: you (the program) give your order to the waiter (the API), who brings back food (data) from the kitchen (the server).

### 2. HTTP basics
| Method | Purpose | Example |
|--------|---------|---------|
| `GET` | read data | get the weather |
| `POST` | create data | create a new post |
| `PUT`/`PATCH` | update data | edit a post |
| `DELETE` | delete data | delete a post |

**Status codes:**
| Code | Meaning |
|------|---------|
| 200 | OK ✅ |
| 201 | Created |
| 400 | Bad request (your fault) |
| 401 / 403 | Not authorised |
| 404 | Not found |
| 429 | Too many requests (slow down!) |
| 500 | Server error (their fault) |

### 3. Your first request
```python
import requests

response = requests.get("https://api.github.com/users/octocat", timeout=10)
print(response.status_code)    # 200
data = response.json()         # JSON → Python dict
print(data["name"], data["public_repos"])
```

### 4. Query parameters
```python
params = {"latitude": 6.52, "longitude": 3.38, "current": "temperature_2m"}
r = requests.get("https://api.open-meteo.com/v1/forecast", params=params, timeout=10)
# Same as: https://api.open-meteo.com/v1/forecast?latitude=6.52&longitude=3.38&current=temperature_2m
```

### 5. POST requests
```python
new_post = {"title": "Hello", "body": "My first post", "userId": 1}
r = requests.post("https://jsonplaceholder.typicode.com/posts", json=new_post, timeout=10)
print(r.status_code)   # 201
print(r.json())
```

### 6. Handling errors
```python
try:
    r = requests.get(url, timeout=10)
    r.raise_for_status()          # raises HTTPError for 4xx/5xx
    data = r.json()
except requests.exceptions.Timeout:
    print("The server took too long.")
except requests.exceptions.ConnectionError:
    print("No internet connection?")
except requests.exceptions.HTTPError as e:
    print(f"Bad response: {e}")
```
Always set a `timeout`, or your program may hang forever.

### 7. Exploring JSON
Real API responses can be big and nested. Explore them step by step:
```python
import json
print(json.dumps(data, indent=2))    # pretty-print
print(data.keys())                   # what's at the top level?
```

### 8. API keys and secrets 🔐
Many APIs need a key. **Never put keys in your code or commit them to GitHub!**

1. Create a file `.env` (already in `.gitignore`):
   ```
   MY_API_KEY=abc123
   ```
2. Load it in Python:
   ```python
   import os
   from dotenv import load_dotenv

   load_dotenv()
   api_key = os.getenv("MY_API_KEY")
   ```
3. Commit a `.env.example` with fake values so others know what's needed.

If you ever commit a key by accident, **revoke it** immediately and make a new one; deleting the commit isn't enough.

### 9. Free APIs to practise with (no key needed)
| API | What it does |
|-----|-------------|
| <https://open-meteo.com> | Weather forecasts |
| <https://jsonplaceholder.typicode.com> | Fake posts/users for practice |
| <https://api.github.com> | GitHub users and repos |
| <https://restcountries.com> | Country info |
| <https://pokeapi.co> | Pokémon data |
| <https://official-joke-api.appspot.com/random_joke> | Random jokes |
| <https://api.dictionaryapi.dev> | Word definitions |

---

## 🧪 Examples
| File | Shows |
|------|-------|
| [`01_first_request.py`](examples/01_first_request.py) | GET, status codes, JSON |
| [`02_params_and_errors.py`](examples/02_params_and_errors.py) | Query params, error handling |
| [`03_post_request.py`](examples/03_post_request.py) | POST with JSON |
| [`04_env_variables.py`](examples/04_env_variables.py) + [`.env.example`](examples/.env.example) | Loading secrets safely |

---

## ✍️ Exercises
| # | File | Difficulty | Task |
|---|------|-----------|------|
| 1 | `ex01_random_joke.py` | ⭐ | Fetch and print a random joke |
| 2 | `ex02_github_profile.py` | ⭐⭐ | Show a GitHub user's profile and top repos |
| 3 | `ex03_country_info.py` | ⭐⭐ | Look up a country's capital, population and currency |
| 4 | `ex04_dictionary.py` | ⭐⭐⭐ | A command-line dictionary with error handling |

---

## 🛠️ Mini-project: Weather CLI App
Create `exercises/weather.py` using the free [Open-Meteo](https://open-meteo.com/en/docs) APIs:
1. Ask for a city name.
2. Use the **geocoding API** to find its latitude and longitude:
   `https://geocoding-api.open-meteo.com/v1/search?name=Lagos&count=1`
3. Use the **forecast API** to get the current temperature, wind speed and a 3-day forecast.
4. Print a nice weather report.
5. Handle: city not found, no internet, timeouts.

**Bonus:**
- Convert weather codes into emojis (☀️ 🌧️ ⛈️)
- Let the user choose °C or °F (`temperature_unit=fahrenheit`)
- Save recent searches to a JSON file
- Structure it into functions (`get_coordinates`, `get_weather`, `format_report`) and write tests for `format_report`

---

## ⚠️ Common mistakes
- Forgetting `timeout=`, so the program hangs.
- Calling `.json()` on an error response; check `status_code` or use `raise_for_status()` first.
- `KeyError` because the JSON structure isn't what you expected. Print it first!
- Committing `.env` or pasting API keys into code. 🚨
- Making requests in a tight loop. Respect rate limits.

## 🔗 Resources
- [requests: Quickstart](https://requests.readthedocs.io/en/latest/user/quickstart/)
- [Real Python: Python and REST APIs](https://realpython.com/api-integration-in-python/)
- [MDN: HTTP status codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)
- [public-apis list on GitHub](https://github.com/public-apis/public-apis)

## ✅ Checklist
- [ ] I can explain what an API, endpoint and status code are
- [ ] I can make a GET request and read the JSON
- [ ] I can pass query parameters
- [ ] I handle timeouts and errors
- [ ] I keep API keys in `.env` and never commit them
- [ ] I built the weather app
