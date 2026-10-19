"""Mini-project solution – Weather CLI using Open-Meteo (no API key needed)."""
import requests

GEOCODE_URL = "https://geocoding-api.open-meteo.com/v1/search"
FORECAST_URL = "https://api.open-meteo.com/v1/forecast"

WEATHER_EMOJI = {
    0: "☀️ Clear", 1: "🌤️ Mainly clear", 2: "⛅ Partly cloudy", 3: "☁️ Overcast",
    45: "🌫️ Fog", 48: "🌫️ Fog", 51: "🌦️ Drizzle", 53: "🌦️ Drizzle", 55: "🌦️ Drizzle",
    61: "🌧️ Rain", 63: "🌧️ Rain", 65: "🌧️ Heavy rain", 80: "🌧️ Showers", 81: "🌧️ Showers",
    82: "⛈️ Violent showers", 95: "⛈️ Thunderstorm", 96: "⛈️ Thunderstorm", 99: "⛈️ Thunderstorm",
}


class WeatherError(Exception):
    pass


def fetch(url, params):
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.Timeout:
        raise WeatherError("The weather service took too long to respond.")
    except requests.exceptions.ConnectionError:
        raise WeatherError("Could not connect. Check your internet.")
    except requests.exceptions.HTTPError as error:
        raise WeatherError(f"The weather service returned an error: {error}")


def get_coordinates(city):
    data = fetch(GEOCODE_URL, {"name": city, "count": 1})
    if not data.get("results"):
        raise WeatherError(f"Couldn't find a city called '{city}'.")
    place = data["results"][0]
    return place["name"], place.get("country", ""), place["latitude"], place["longitude"]


def get_weather(lat, lon, unit="celsius"):
    return fetch(FORECAST_URL, {
        "latitude": lat,
        "longitude": lon,
        "current": "temperature_2m,wind_speed_10m,weather_code",
        "daily": "temperature_2m_max,temperature_2m_min,weather_code",
        "forecast_days": 3,
        "temperature_unit": unit,
        "timezone": "auto",
    })


def describe(code):
    return WEATHER_EMOJI.get(code, "🌈 Mixed")


def format_report(name, country, weather, symbol="°C"):
    current = weather["current"]
    daily = weather["daily"]
    lines = [
        f"\n📍 {name}, {country}",
        f"Now: {describe(current['weather_code'])}  {current['temperature_2m']}{symbol}  "
        f"💨 {current['wind_speed_10m']} km/h",
        "\n3-day forecast:",
    ]
    for day, high, low, code in zip(
        daily["time"], daily["temperature_2m_max"], daily["temperature_2m_min"], daily["weather_code"]
    ):
        lines.append(f"  {day}  {describe(code):<20} {low}{symbol} – {high}{symbol}")
    return "\n".join(lines)


def main():
    unit = "fahrenheit" if input("Units: (c)elsius or (f)ahrenheit? ").lower() == "f" else "celsius"
    symbol = "°F" if unit == "fahrenheit" else "°C"
    while True:
        city = input("\nCity (or 'quit'): ").strip()
        if city.lower() == "quit":
            break
        try:
            name, country, lat, lon = get_coordinates(city)
            print(format_report(name, country, get_weather(lat, lon, unit), symbol))
        except WeatherError as error:
            print(f"❌ {error}")


if __name__ == "__main__":
    main()
