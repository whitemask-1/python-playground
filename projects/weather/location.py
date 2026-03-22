import os

def check_for_current_location():
    current_directory = os.path.dirname(__file__)
    config_dir = os.path.join(current_directory, "current_location.json")

    if os.path.exists(config_dir):
        with open(config_dir) as config_file:
            current_location = config_file.read()
            return current_location
    else:
        with open(config_dir, "w") as config_file:
            user_location = input("Enter current location")
            config_file.write(f'"location":{user_location}')
            return user_location
