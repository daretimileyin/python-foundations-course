import requests

country = input("Country: ").strip()
response = requests.get(f"https://restcountries.com/v3.1/name/{country}", timeout=10)

if response.status_code == 404:
    print("Country not found.")
else:
    response.raise_for_status()
    info = response.json()[0]
    currencies = ", ".join(f"{c['name']} ({c.get('symbol', '')})" for c in info.get("currencies", {}).values())
    languages = ", ".join(info.get("languages", {}).values())

    print(f"\n🌍 {info['name']['official']}")
    print(f"Capital:    {', '.join(info.get('capital', ['N/A']))}")
    print(f"Region:     {info['region']}")
    print(f"Population: {info['population']:,}")
    print(f"Currencies: {currencies}")
    print(f"Languages:  {languages}")
