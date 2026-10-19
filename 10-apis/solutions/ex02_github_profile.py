import requests

username = input("GitHub username: ").strip()
base = f"https://api.github.com/users/{username}"

response = requests.get(base, timeout=10)
if response.status_code == 404:
    print(f"No GitHub user called '{username}'.")
else:
    response.raise_for_status()
    user = response.json()
    print(f"\n👤 {user['name'] or username}")
    print(f"   {user['bio'] or '(no bio)'}")
    print(f"📍 {user['location'] or 'Unknown'}")
    print(f"👥 {user['followers']} followers | 📦 {user['public_repos']} public repos")

    repos = requests.get(f"{base}/repos", params={"per_page": 100}, timeout=10).json()
    top = sorted(repos, key=lambda r: r["stargazers_count"], reverse=True)[:5]
    print("\nTop repositories:")
    for repo in top:
        print(f"  ⭐ {repo['stargazers_count']:>5}  {repo['name']}")
