# json.load() and json.dump() turn structured data into JSON outputs and vice versa.
# They are part of the built-in json module in Python.
import json
# Example of using json.dump() to write JSON data to a file
data = {
    "id": 123,
    "name": "John Doe",
    "signup_ts": "2023-10-10T10:00:00",
    "friends": [1, 2, 3]
}
with open('user_data.json', 'w') as f:
    json.dump(data, f)

# Example of using json.load() to read JSON data from a file
with open('user_data.json', 'r') as f:
    loaded_data = json.load(f)
    print("Loaded data:", loaded_data)

# Example of using json.dumps() to convert a Python object to a JSON string
json_string = json.dumps(data)
print("JSON string:", json_string)

# Example of using json.loads() to convert a JSON string back to a Python object
python_object = json.loads(json_string)
print("Python object:", python_object)

# Note: json.dump() and json.load() work with file objects, while json.dumps() and json.loads() work with strings.
# json.load() and json.dump() turn structured data into JSON outputs and vice versa.
# json.loads() and json.dumps() turn structured data into JSON strings and vice versa.