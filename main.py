import os
from weather.fetcher import get_weather

if __name__ == "__main__":
    city = input("Enter city: ")
    api_key = os.getenv("WEATHER_API_KEY")  # set this in your GitHub Secrets
    weather = get_weather(city, api_key)
    print(f"{weather['city']}: {weather['temp']}°C, {weather['description']}")
