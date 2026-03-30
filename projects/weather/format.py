from datetime import datetime, timezone, timedelta
from dataclasses import dataclass, field, asdict
from pathlib import Path
import json
from typing import Any

PROFILES_PATH = Path(__file__).parent / "weather_prefs.json"

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
            raise ValueError(f"Unknown fields: {invalid_fields}. \
                             Valid: {VALID_FIELDS}")
        if self.unit_system not in VALID_UNIT_SYSTEMS:
            raise ValueError(f"Unit system must be one of {VALID_UNIT_SYSTEMS}")

def _load_all() -> dict:
    """Load profiles. Returns empty dict if file doesnt exist"""
    if not PROFILES_PATH.exists():
        return {}
    return json.loads(PROFILES_PATH.read_text())

def _save_all(profiles: dict) -> None:
    """Write profiles dict to file"""
    PROFILES_PATH.write_text(json.dumps(profiles, indent=2))

def _prefs_to_dict(prefs: WeatherPrefs) -> dict:
    """Serialize Prefs to a json-safe dict"""
    return {
            "fields": list(prefs.fields),
            "unit_system": prefs.unit_system
    }

def _dict_to_prefs(data: dict) -> WeatherPrefs:
    """Deserialize stored dict to WeatherPrefs instance"""

    return WeatherPrefs(
            fields=set(data["fields"]),
            unit_system=data["unit_system"]
    )

def create_profile(name: str, prefs: WeatherPrefs) -> None:
    """Save new profile, prompt for confirmation if name exists"""

    profiles = _load_all()

    if name in profiles:
        confirm = input(f"Profile '{name}' already exists. Overwrite? (y/n): ")
        if confirm != "y":
            raise ValueError(f"Aborted - profile '{name}' was not overwritten.")

    profiles[name] = _prefs_to_dict(prefs)
    _save_all(profiles)
    print(f"Profile '{name}' saved.")

def load_profile(name: str) -> WeatherPrefs:
    """Load profile and return WeatherPrefs object"""

    profiles = _load_all()
    if name not in profiles:
        raise KeyError(f"No profile named '{name}'. \
                       Available: {list(profiles.keys())}")

    return _dict_to_prefs(profiles[name])

def edit_profile(name: str, **kwargs) -> None:
    """
    Update fields of an existing profile
    Valid kwargs: 'fields' (set[str]), 'unit_system' (str) 
    """

    profiles = _load_all()
    if name not in profiles:
        raise KeyError(f"No profile named '{name}'. \
                       Available: {list(profiles.keys())}")

    current = _dict_to_prefs(profiles[name])

    if "fields" in kwargs:
        current.fields = kwargs["fields"]
    if "unit_system" in kwargs:
        current.unit_system = kwargs["unit_system"]

    current.__post_init__()

    profiles[name] = _prefs_to_dict(current)
    _save_all(profiles)
    print(f"Profile '{name}' updated.")

def delete_profile(name: str) -> None:
    """Delete named profile if it exists"""
    profiles = _load_all()
    if name not in profiles:
        raise KeyError(f"No profile named '{name}'. \
                        Available: {list(profiles.keys())}")

    confirm = input(f"Delete profile '{name}'? This cannot be undone. (y/n): ")
    if confirm != "y":
        print("Aborted.")
        return

    del profiles[name]
    _save_all(profiles)
    print(f"Profile '{name}' deleted.")

def list_profiles() -> list[str]:
    """Return all saved profile names"""
    return list(_load_all().keys())

def parse_weather_response(data: dict[str, Any]) -> dict[str, Any]:
    """
    Parse API response into human readable dict with 
    unit conversion and timestamp localization
    """

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

def get_weather_output(parsed: dict, profile_name: str) -> str:
    """Load named profile and return formatted weather output"""
    prefs = load_profile(profile_name)
    return format_weather(parsed, prefs)
