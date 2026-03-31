import os
import requests
from typing import Any
from dotenv import load_dotenv

load_dotenv()
weather_api_key = os.getenv("WEATHER_API_KEY")

def get_weather_from_coords(coordinates: tuple[float, float]) -> dict[str, Any]:
    """Use latitude and longitude to query the API for a weather overview"""

    params = {"lat":coordinates[0], "lon":coordinates[1], "appid":weather_api_key}
    try:
        weather_request = requests.get(
                "https://api.openweathermap.org/data/2.5/weather",
                params=params
                )
        data = weather_request.json()
        if not data:
            raise ValueError(f"No results found  \
                             for {coordinates[0]} and {coordinates[1]}")
        return data

    except requests.RequestException as err:
        raise RuntimeError(f"Weather Overview API unreachable: {err}") from err

