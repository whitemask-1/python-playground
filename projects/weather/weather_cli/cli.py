import argparse
import sys
from pathlib import Path
from weather_cli.profiles import (
        create_profile, load_profile, edit_profile,
        delete_profile, list_profiles, WeatherPrefs,
        VALID_UNIT_SYSTEMS, VALID_FIELDS
)
from weather_cli.printout import format_weather, parse_weather_response
from weather_cli.location import check_for_current_location
from weather_cli.api import get_weather_from_coords

def build_parser() -> argparse.ArgumentParser:

    parser = argparse.ArgumentParser(
            prog="weather",
            description="Fetch and display weather with saved preference profiles."
    )

    parser.add_argument(
            "-p", "--profile",
            metavar="NAME",
            help="Use a saved preference profile by name"
    )

    parser.add_argument(
            "--set-location", "-l",
            action="store_true",
            help="Clear saved location and re-enter interactively."
    )

    parser.add_argument(
            "--new-profile", "-n",
            metavar="NAME",
            help="Create a new preference profile with the given name."
    )
    parser.add_argument(
            "--edit-profile", "-e",
            metavar="NAME",
            help="Edit an existing profile by name."
    )
    parser.add_argument(
            "--delete-profile", "-d",
            metavar="NAME",
            help="Delete a profile by name."
    )
    parser.add_argument(
            "--list-profiles",
            action="store_true",
            help="List all saved profile names."
    )
    
    parser.add_argument(
            "--fields",
            nargs="+",
            metavar="FIELD",
            help=f"Fields to display. Valid: {', '.join(sorted(VALID_FIELDS))}"
    )
    parser.add_argument(
            "--units",
            choices=["metric", "imperial"],
            help="Unit system for the profile"
    )

    return parser

def handle_new_profile(name: str, args: argparse.Namespace) -> None:
    fields = set(args.fields) if args.fields else None
    unit_system = args.units if args.units else "imperial"

    if fields:
        prefs = WeatherPrefs(fields=fields, unit_system=unit_system)
    else:
        print(f"Creating profile '{name}'.")
        print(f"Available fields: {', '.join(sorted(VALID_FIELDS))}")
        raw = input("Enter fields to display (space-separated), \
                    or press Enter for defaults: ").strip()
        fields = set(raw.split()) if raw else None

        raw_units = input("Unit system  \
                          - metric or imperial (default: imperial): ").strip().lower()
        unit_system = raw_units if raw_units in VALID_UNIT_SYSTEMS else "imperial"

        prefs = WeatherPrefs(
                fields = fields if fields 
                else WeatherPrefs.__dataclass_fields__["fields"].default_factory(),
                unit_system=unit_system
        )

    create_profile(name, prefs)

def handle_edit_profile(name: str, args: argparse.Namespace) -> None:
    kwargs = {}
    if args.fields:
        kwargs["fields"] = set(args.fields)
    if args.units:
        kwargs["unit_system"] = args.units

    if not kwargs:
        print(f"Editing profile '{name}'. Press Enter to keep value.")
        raw_fields = input(f"New fields (space-separated)  \
                           [{', '.join(sorted(VALID_FIELDS))}]: ").strip()

        raw_units = input("New unit system (metric/imperial): ").strip().lower()

        if raw_fields:
            kwargs["fields"] = set(raw_fields.split())
        if raw_units in VALID_UNIT_SYSTEMS:
            kwargs["unit_system"] = raw_units

    if kwargs:
        edit_profile(name, **kwargs)
    else:
        print("Nothing to update.")

def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    if args.list_profiles:
        profiles = list_profiles()
        if profiles:
            print("Saved profiles: " + ", ".join(profiles))
        else:
            print("No profiles saved.")
        return

    if args.new_profile:
        handle_new_profile(args.new_profile, args)
        return

    if args.edit_profile:
        handle_edit_profile(args.edit_profile, args)
        return

    if args.delete_profile:
        delete_profile(args.delete_profile)
        return

    if args.set_location:
        location_path = Path(__file__).parent / "current_location.json"
        if location_path.exists():
            location_path.unlink()

    try:
        lat, lon = check_for_current_location()
    except ValueError:
        print("No location set. Exiting.", file=sys.stderr)
        sys.exit(1)

    if args.profile:
        try:
            prefs = load_profile(args.profile)
        except KeyError as e:
            print(f"Error: {e}", file=sys.stderr)
            sys.exit(1)
    else:
        prefs = WeatherPrefs()

    raw = get_weather_from_coords((lat, lon))
    parsed = parse_weather_response(raw)
    print(format_weather(parsed, prefs))
    print(f"[stub] Fetching weather for ({lat}, {lon}) \
          with profile '{args.profile or 'default'}'")




