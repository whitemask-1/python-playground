# Fields allow you customize and add metadata to individual attributes within Pydantic models.
# There are also Field parameters which allow you to set constraints and validation rules for specific fields

# Some of these parameters include:
#       default: Sets a default value for the field if none is provided during instantiation.
#       default_factory: A callable that generates a default value for the field.
#       alias: An alternative name for the field when serializing/deserializing data.
#       title: A human-readable title for the field, useful for documentation.
#       description: A detailed description of the field, useful for documentation.
#       const: If set to True, the field value cannot be changed after instantiation.
#       gt, ge, lt, le: Greater than, greater than or equal to, less than, less than constraints for numeric fields.
#       min_length, max_length: Minimum and maximum length constraints for string and list fields.
#       regex: A regular expression that the field value must match (for string fields).
#       example: An example value for the field, useful for documentation and testing.
#       frozen: If set to True, the field value cannot be modified after instantiation (similar to const but for mutable types).
#       repr: A custom representation function for the field, used when printing or logging the model.
#       pattern: A pattern that the field value must match (for string fields, similar to regex).
#       deprecated: If set to True, indicates that the field is deprecated and should not be used in new code.

from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime

class User(BaseModel):
    id: int = Field(..., title="ID", description="The unique identifier for the user") # The ... indicates that this field is required
    name: str = Field(..., title="Name", description="The name of the user", min_length=1, max_length=50)
    signup_ts: datetime | None = Field(None, title="Signup Timestamp", description="The timestamp when the user signed up")
    friends: list[int] = Field([], title="Friends", description="List of friend IDs", min_length=0)

    model_config = ConfigDict(
        validate_assignment=True,  # Validate data on assignment to attributes
    )

# Example usage
user = User(id=1, name="Alice", signup_ts="2024-01-01T12:00:00", friends=[2, 3, 4])
print(user)
print(user.model_dump())  # Serialize to dictionary
print(user.model_dump_json())  # Serialize to JSON string