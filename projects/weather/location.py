import os

def load_current_location():
    current_directory = os.path.dirname(__file__)
    print(current_directory)

load_current_location()
