from datetime import datetime, timezone, timedelta
from dataclasses import dataclass, field
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

VALID_FIELDS = {
        "location", "conditions", "temperature", "feels_like", 
        "humidity", "pressure", "visibility", "wind", "clouds", 
        "timestamps"
}

VALID_UNIT_SYSTEMS = {"metric", "imperial"}

@dataclass
class WeatherPrefs:
    fields: set[str] = field(default_factory=lambda: {
        "location", "conditions", "temperature", 
        "humidity", "wind", "clouds","timestamps"
        })

    unit_system: str = "imperial"

    def __post_init__(self):
        invalid_fields = self.fields - VALID_FIELDS
        if invalid_fields:
            raise ValueError(f"Unknown fields: {invalid_fields}. Valid: {VALID_FIELDS}")
        if self.unit_system not in VALID_UNIT_SYSTEMS:
            raise ValueError(f"Unit system must be one of {VALID_UNIT_SYSTEMS}")

def format_weather(parsed: dict, prefs: WeatherPrefs) -> str:
    """Using user preferences and the weather overview dict 
        return a formatted weather string"""
    
    metric = prefs.unit_system == "metric"
    lines = []

    def _degrees_to_cardinal(deg: int) -> str:
        directions = ["N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE",
                  "S", "SSW", "SW", "WSW", "W", "WNW", "NW", "NNW"]
        index = round(deg / 22.5) % 16
        return directions[index]

    if "location" in prefs.fields:
        loc = parsed["location"]
        lines.append(f"{loc['name']}, {loc['country']}")

    if "conditions" in prefs.fields:
        descs = ", ".join(c["description"] for c in parsed["conditions"])
        lines.append(f"Conditions: {descs}")

    if "temperature" in prefs.fields:
        t = parsed["temperature"]
        temp = t["celsius"] if metric else t["fahrenheit"]
        unit = "°C" if metric else "°F"
        lines.append(f"Temp: {temp}{unit}")

    if "feels_like" in prefs.fields:
        t = parsed["temperature"]
        feels_like_temp = t["feels_like_c"] if metric else t["feels_like_f"]
        unit = "°C" if metric else "°F"
        lines.append(f"Feels like: {feels_like_temp}{unit}")
        
    if "humidity" in prefs.fields:
        lines.append(f"Humidity: {parsed['atmosphere']['humidity_pct']}%")

    if "pressure" in prefs.fields:
        lines.append(f"Pressure: {parsed['atmosphere']['pressure_hpa']} hPa")

    if "visibility" in prefs.fields:
        vis = parsed["atmosphere"]["visibility_meters"]
        if vis is not None:
            distance = round(vis / 1000, 2) if metric else round(vis / 1609.34, 2)
            unit = "km" if metric else "mi"
            lines.append(f"Visibility: {distance}{unit}")

    if "wind" in prefs.fields:
        w = parsed["wind"]
        speed = w["speed_mps"] if metric else w["speed_mph"]
        unit = "m/s" if metric else "mph"
        if w["deg"] is not None:
            cardinal = _degrees_to_cardinal(w["deg"])
            lines.append(f"Wind: {speed} {unit} from {cardinal} ({w['deg']}°)")
        else:
            lines.append(f"Wind: {speed} {unit}, direction unavailable")

    if "clouds" in prefs.fields:
        lines.append(f"Cloud cover: {parsed['atmosphere']['cloud_cover_pct']}%")

    if "timestamps" in prefs.fields:
        ts = parsed["timestamps"]
        lines.append(f"Observed at: {ts['observed']}")
        lines.append(f"Sunrise: {ts['sunrise']} \n Sunset: {ts['sunset']}")

    return "\n".join(lines)
