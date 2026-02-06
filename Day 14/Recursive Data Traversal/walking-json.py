# Walking through a JSON structure recursively
import json
def walk_json(data, indent=0): # Indent parameter to track the current level of indentation and therefore the nesting level
    spacing = '  ' * indent
    if isinstance(data, dict): # Check if the data that was passed is a dictionary
        for key, value in data.items(): # For each key-value pair in the dictionary, print the spacing before the key and the key
            print(f"{spacing}{key}:")
            walk_json(value, indent + 1) # Then walk through the value associated with that key, increase indentation by 1, and call the function with the value as the new data to be processed
    elif isinstance(data, list): # Check if the data that was passed is a list
        for index, item in enumerate(data): # For each item in the list, print the indentation at that level and the index of the item
            print(f"{spacing}[{index}]:") 
            walk_json(item, indent + 1) # Then walk through the item as the new data to be processed, increasing the indentation by 1
    else:
        print(f"{spacing}{data}")

# Note that the else statement unwinds the recursion when a primitive data type (string, number, boolean, etc.) is reached and simply prints the value with the appropriate indentation.
# But how is the next line after the primitive value processed?
# When the function call for the primitive value completes, the function returns to the previous call in the call stack, which was processing either a dictionary or a list.
# The loop in that previous call then continues to the next key-value pair (for a dictionary) or the next item (for a list), and the process repeats until all items have been processed.
# Essentially this is powered by the for loops in the dictionary and list cases, which continue iterating after each recursive call returns.

# Example JSON data
json_data = '''
{
    "name": "John",
    "age": 30,
    "cars": [
        {
            "model": "Ford",
            "mpg": 25.5
        },
        {
            "model": "BMW",
            "mpg": 26.5
        }
    ],
    "address": {
        "street": "123 Main St",
        "city": "New York"
    }
}
'''

data = json.loads(json_data) # Parse JSON string into Python data structure
walk_json(data)  # Walk through and print the JSON structure

