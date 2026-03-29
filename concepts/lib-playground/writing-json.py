import json
import os

current_dir = os.path.dirname(__file__)
practice_json = os.path.join(current_dir, "practice.json")

with open(practice_json, "w") as dump_to_file:
        json.dump([35.6,12.4], dump_to_file)

with open(practice_json) as config_file:
            current_location = json.load(config_file)

print(current_location)

print(current_dir)

