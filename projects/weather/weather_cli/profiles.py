from pathlib import Path
from dataclasses import dataclass, field
import json

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


