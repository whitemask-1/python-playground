from pydantic import ConfigDict, BaseModel

#Configuration settings for Pydantic models allow you to customize the behavior of the models with more flexibility that normally offered by Pythonic classes.
# Some of the things that are different from normal Python classes include:
# Validation: Pydantic models automatically validate data types and constraints when creating instances, ensuring that the data adheres to the defined schema.
# Serialization: Pydantic models provide built-in methods for serializing and deserializing data
# Immutable Models: Pydantic allows you to create immutable models, where the attributes cannot be changed after instantiation.
# Custom Validation: Pydantic supports custom validation logic through validators, allowing you to define complex validation rules for your models.
# ORM Integration: Pydantic models can be easily integrated with Object-Relational Mappers (ORMs) for database interactions.
# Performance Optimization: Pydantic is designed for high performance, making it suitable for applications that require fast data processing.
# Type Hints: Pydantic leverages Python's type hints to define the structure of models, making it easier to understand and maintain the code.
# Type Coercion: Pydantic can automatically coerce types when possible, converting input data to the expected types defined in the model.

class User(BaseModel):
    id: int
    name: str
    signup_ts: str | None = None
    friends: list[int] = []

    model_config = ConfigDict(
        title="User Model",
        str_strip_whitespace =True,  # Automatically strip whitespace from string fields
        str_min_length =1,            # Minimum length for any string field
        str_max_length=50,           # Maximum length for any string field
        validate_assignment=True,       # Validate data on assignment to attributes
        use_enum_values=True,           # Use enum values instead of enum instances
        json_encoders={                 # Custom JSON encoders for specific types
            str: lambda v: v.upper()   # Example: Convert all strings to uppercase during serialization
        }
    )

# Example usage
user = User(id=1, name = " Kevin", signup_ts="2024-01-01T12:00:00", friends=[2, 3, 4]) # Notice the whitespace in the name
print(user)
print(user.model_dump_json())  # Serialize to JSON, name should be in uppercase due to custom encoder

# You can use .model_dump() method to serialize the model to a dictionary
# and .model_dump_json() to serialize to JSON string