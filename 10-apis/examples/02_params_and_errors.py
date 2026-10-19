"""Example 02 – Query parameters and error handling."""
import requests

GEOCODE_URL = "https://geocoding-api.open-meteo.com/v1/search"
FORECAST_URL = "https://api.open-meteo.com/v1/forecast"


def get_json(url, params):
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.Timeout:
        print("⏱️ The request timed out.")
    except requests.exceptions.ConnectionError:
        print("📡 Could not connect. Are you online?")
    except requests.exceptions.HTTPError as error:
        print(f"❌ HTTP error: {error}")
    return None


city = input("City: ")
places = get_json(GEOCODE_URL, {"name": city, "count": 1})

if places and places.get("results"):
    place = places["results"][0]
    print(f"Found {place['name']}, {place.get('country')} at ({place['latitude']}, {place['longitude']})")

    weather = get_json(FORECAST_URL, {
        "latitude": place["latitude"],
        "longitude": place["longitude"],
        "current": "temperature_2m,wind_speed_10m",
    })
    if weather:
        current = weather["current"]
        print(f"🌡️ {current['temperature_2m']}°C   💨 {current['wind_speed_10m']} km/h")
else:
    print("City not found.")

# What a 404 looks like
print("\nRequesting a page that doesn't exist:")
get_json("https://api.github.com/users/this-user-should-not-exist-12345", {})
