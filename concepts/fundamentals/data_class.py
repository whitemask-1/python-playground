#What is @dataclass?
# The @dataclass decorator is a built-in feature in Python that automatically generates special methods like __init__(), __repr__(), and __eq__() for classes.
# It simplifies the process of creating classes that are primarily used to store data by reducing boilerplate code.
from dataclasses import dataclass, field
from datetime import datetime

@dataclass
class User: # Notice there is no __init__ method defined, it is generated automatically
    id: int
    name: str
    signup_ts: datetime | None = None  # Set a default value of None
    friends: list[int] = field(default_factory=list)  # Set a default value of an empty list
# The field function with default_factory is used to provide a default value for mutable types like lists. However they can use multiple arguments to customize the field behavior.
# Think of a field as a range of attributes that can be applied to each attribute in a dataclass.

# Example of valid data
valid_data = {
    "id": 123,
    "name": "John Doe",
    "signup_ts": datetime.now(),
    "friends": [1, 2, 3]
}

# Create User instance with valid data
user_valid = User(**valid_data)
print("Valid data:", user_valid)

