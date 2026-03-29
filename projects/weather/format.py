from datetime import datetime, timezone, timedelta
from typing import Any
import location
import api

def parse_weather_response(data: dict[str, Any]) -> dict[str, Any]:
    """Parse API response into human readable dict with unit conversion and timestamp localization"""

    tz_offset_seconds = data["timezone"]
    local_tz = timezone(timedelta(seconds=tz_offset_seconds))

    def unix_to_local(ts: int) -> str:
        """Convert Unix timestamp to location local time"""
        return datetime.fromtimestamp(ts, tz=local_tz).strftime("%Y-%m-%d %H:%M:%S %Z")

    def kelvin_to_celsius(k: float) -> float:
        return round(k - 273.15, 1)

    def kelvin_to_fahrenheit(k: float) -> float:
        return round((k - 273.15) * 9/5 + 32, 1)

    main = data["main"]
    sys = data["sys"]
    wind = data["wind"]

    conditions = [
        {
            "id": w["id"],
            "main": w["main"],
            "description": w["description"]
        }
        for w in data["weather"]
    ]

    return {
        "location": {
            "name": data["name"],
            "country": sys["country"],
            "lat": data["coord"]["lat"],
            "lon": data["coord"]["lon"]
        },
        "conditions": conditions,
        "temperature": {
            "celsius": kelvin_to_celsius(main["temp"]),
            "fahrenheit": kelvin_to_fahrenheit(main["temp"]),
            "feels_like_c": kelvin_to_celsius(main["feels_like"]),
            "feels_like_f": kelvin_to_fahrenheit(main["feels_like"]),
            "min_c": kelvin_to_celsius(main["temp_min"]),
            "max_c": kelvin_to_celsius(main["temp_max"]),
            "min_f": kelvin_to_fahrenheit(main["temp_min"]),
            "max_f": kelvin_to_fahrenheit(main["temp_max"])
        },
        "atmosphere": {
            "humidity_pct": main["humidity"],
            "pressure_hpa": main["pressure"],
            "sea_level_hpa": main.get("sea_level"), #optional API output
            "grnd_level_hpa": main.get("grnd_level"),#^
            "visibility_meters": data.get("visibility"),#^
            "cloud_cover_pct": data["clouds"]["all"]
        },
        "wind": {
            "speed_mps": wind["speed"],
            "speed_mph": round(wind["speed"] * 2.23694, 2),
            "deg": wind.get("deg"), #optional API output
            "gust_mps": wind.get("gust")
        },
        "timestamps": {
            "observed": unix_to_local(data["dt"]),
            "sunrise": unix_to_local(sys["sunrise"]),
            "sunset": unix_to_local(sys["sunset"])
        }
    }

current_loc = location.check_for_current_location()
weather_data = api.get_weather_from_coords(current_loc)
parsed = parse_weather_response(weather_data)
print(parsed)
