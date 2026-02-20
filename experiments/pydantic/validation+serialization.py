# Validation is pydantic's core feature and reason for the BaseModel class existence.
# It ensures that the data being processed adheres to the defined schema and constraints and will flexibly handle various data types and structures.
# By that I mean it will try to coerce the data into the expected types when possible.

# Serialization is the process of converting a Pydantic model instance into a format which can be stored or transmitted, such as JSON or a dictionary.
# Pydantic provides built-in methods for serializing models, making it easy to convert them to and from different formats.
# This is particularly useful for APIs, data storage, and inter-process communication.
# For example, you can use the .model_dump() method to serialize the model to a dictionary
# and .model_dump_json() to serialize to JSON string.

# I will go through an example of both validation and serialization and point out where they happen and how they work within the syntax of Pydantic models.
from pydantic import BaseModel, ConfigDict
from datetime import datetime

class User(BaseModel):
    id: int
    name: str
    signup_ts: str | None = None # Union operator to allow a default value of None, which makes this field optional, notice name and id are not optional
    friends: list[int] = []
    # Pydantic will validate the types of the fields when creating an instance of the model
    model_config = ConfigDict(
        validate_assignment=True,  # Validate data on assignment to attributes
        json_encoders={            # Custom JSON encoders for specific types
            datetime: lambda v: v.isoformat()  # Example: Convert datetime to ISO format string during serialization
        }
    )
    
# Example usage
user = User(id=1, name="John Doe", signup_ts="2024-01-01T12:00:00", friends=[2, 3, 4])
print(user)
# At this point, Pydantic has validated the input data types and coerced the signup_ts string into a datetime object if needed.

# Now let's serialize the model to a dictionary and JSON
user_dict = user.model_dump()  # Serialize to dictionary
print(user_dict)
user_json = user.model_dump_json()  # Serialize to JSON string
print(user_json)

# I've also seen that people have trouble finding code at their literacy level however in VS Code you can select any text and right click to "Explain" which will allow Copilot to generate an explanation for you.
# This is useful for understanding code snippets that may be complex or unfamiliar.

# Additionally, Pydantic supports validation on assignment if configured, meaning that if you change an attribute after instantiation, it will re-validate the new value.
user.name = "Jane Doe"  # This will trigger validation for the name field
print(user)