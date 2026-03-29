import os
import json
import requests
from dotenv import load_dotenv
from typing import Tuple


load_dotenv()
weather_api_key = os.getenv("WEATHER_API_KEY")

def check_for_current_location() -> tuple[float,float]: 
    """Source the current location file for current coordinates + configuration"""

    current_directory = os.path.dirname(__file__)
    config_dir = os.path.join(current_directory, "current_location.json")

    if os.path.exists(config_dir):
        with open(config_dir) as config_file:
            current_location = json.load(config_file)
            lat, lon = current_location
            return lat, lon
    else:
        while True:

            user_input = []
            country_code = input("Enter Country Code (e.g. UK or US): ")
            user_input.append(country_code)

            if country_code.lower() in ("q", "quit"):
                break

            elif country_code == "US":
                state_code = input("Enter State Code (e.g. NC or AZ): ")
                user_input.insert(0, state_code)

                if state_code.lower() in ("q", "quit"):
                    break

            city_code = input("Enter City (e.g. London or Brooklyn): ")
            user_input.insert(0, city_code)

            if city_code.lower() in ("q", "quit"):
                break

            try:
                lat, lon = _geocode_align(", ".join(user_input))
                with open(config_dir, "w") as config_file:
                    json.dump([lat,lon], config_file)
                print("Success")
                return lat, lon

            except (ValueError, RuntimeError) as e:
                print(f"Error: {e}. Try again.")
                continue
    raise ValueError("Bye Bye")

                


def _geocode_align(user_location: str):
    """Use Geocode API to convert input location into coordinates for the Weather API"""

    params = {"q" : user_location, "limit" : 1, "appid" : weather_api_key}
    try:
        geo_response = requests.get(
                "https://api.openweathermap.org/geo/1.0/direct", 
                params=params
        )
        geo_response.raise_for_status()
        data = geo_response.json()

        if not data:
            raise ValueError(f"No results found for {user_location}, \
                             please review input structure")

        return data[0]["lat"], data[0]["lon"]

    except requests.RequestException as err:
        raise RuntimeError(f"Geocoding API unreachable: {err}") from err



print(type(check_for_current_location()))
