from dotenv import load_dotenv
from pprint import pprint
import requests
import os

# Load environment variables from .env file
load_dotenv()


def get_current_weather(city="Colombo"):
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("API_KEY environment variable is not set.")

    request_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=imperial"

    response = requests.get(request_url)

    if response.status_code != 200:
        raise Exception(
            f"Error fetching weather data: {response.status_code}, {response.text}"
        )

    weather_data = response.json()

    return weather_data


if __name__ == "__main__":
    print("\n** Weather App **\n")

    city = input("Please enter a city: ")

    try:
        weather_data = get_current_weather(city)
        pprint(weather_data)
    except Exception as e:
        print(f"An error occurred: {e}")
