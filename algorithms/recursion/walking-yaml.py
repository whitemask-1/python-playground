# Walking through a YAML structure recursively
import yaml

def walk_yaml(data, indent=0): # Indent parameter to track nesting level
    spacing = '  ' * indent
    if isinstance(data, dict): # Check if the data is a dictionary
        for key, value in data.items(): # For each key-value pair in the dictionary
            print(f"{spacing}{key}:")
            walk_yaml(value, indent + 1) # Recursively walk through the value, increasing indentation
    elif isinstance(data, list): # Check if the data is a list
        for index, item in enumerate(data): # For each item in the list
            print(f"{spacing}[{index}]:")
            walk_yaml(item, indent + 1) # Recursively walk through the item, increasing indentation
    else:
        print(f"{spacing}{data}") # Print primitive data types with appropriate indentation

# Example YAML data
yaml_data = '''
name: John
age: 30
cars:
  - model: Ford
    mpg: 25.5
  - model: BMW
    mpg: 26.5
address:
  street: 123 Main St
  city: New York
'''

data = yaml.safe_load(yaml_data)  # Parse YAML string into Python data structure
walk_yaml(data)  # Walk through and print the YAML structure

# Note that this function works similarly to the JSON walking function, handling dictionaries and lists recursively.
# The recursion unwinds when a primitive data type is reached, printing the value and returning to the previous level in the call stack.