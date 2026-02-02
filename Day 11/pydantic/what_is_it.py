# What is pydantic?
# Pydantic is a data validation library so that the user can define how data should be structured and then validate it.
# It uses Python type annotations to define the structure of the data.
from pydantic import BaseModel, ValidationError
from datetime import datetime

# Define a Pydantic model
class User(BaseModel):
    id : int
    name : str
    signup_ts : datetime | None = None #Set a default value of None
    friends : list[int] = [] #Set a default value of an empty list

# Example of valid data
valid_data = {
    "id": 123,
    "name": "John Doe",
    "signup_ts": datetime.now(),
    "friends": [1, 2, 3]
}

# Example of invalid data
invalid_data = {
    "id": "not_an_integer",  # This should be an integer
    "name": "Jane Doe",
    "signup_ts": "2023-10-10T10:00:00",
    "friends": ["not_an_integer"]  # This should be a list of integers
}

# Validate valid data
try:
    user = User(**valid_data)
    print("Valid data:", user)
except ValidationError as e:
    print("Validation error for valid data:", e)

# Validate invalid data
try:
    user = User(**invalid_data)
    print("Invalid data:", user)    
except ValidationError as e:
    print("Validation error for invalid data:", e)

