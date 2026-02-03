# Pydantic dataclasses provide a way to define data structures with validation and serialization capabilities using Python's dataclass syntax.
# They combine the benefits of dataclasses with Pydantic's powerful data validation features.

from pydantic.dataclasses import dataclass
from pydantic import ValidationError, Field

# Pydantic dataclasses are initialized using the @dataclass decorator from pydantic.dataclasses

@dataclass
class User:
    id: int
    name: str
    signup_ts: str | None = None
    friends: list[int] = Field(default_factory=list) # Note: to set this as a list you must use default_factory, not just = [], however in Pydantic BaseModel you can just use = []

# Example usage
try:
    user = User(id=1, name="Alice", signup_ts="2024-01-01T12:00:00", friends=[2, 3, 4])
    print("User created successfully:", user)
except ValidationError as e:
    print("Validation Error:", e)

# What makes it different from BaseModel is that you can use it with other libraries that expect standard dataclasses as input.
# Additionally, Pydantic dataclasses support all the same validation features as Pydantic models, including type coercion and custom validation logic.
# However, they do not support some features specific to BaseModel, such as model configuration via ConfigDict.
# Pydantic dataclasses are useful when you want to leverage Pydantic's validation capabilities while maintaining compatibility with libraries that use standard dataclasses.

# the rebuild_dataclass function can be used to convert existing dataclasses into Pydantic dataclasses, enabling validation for pre-defined data structures. however the data structure probably should already be defined using the pydantic dataclass decorator.
from pydantic.dataclasses import rebuild_dataclass
from dataclasses import dataclass as std_dataclass

@std_dataclass
class StandardUser:
    id: int
    name: str
    signup_ts: str | None = None
    friends: list[int] = []

PydanticUser = rebuild_dataclass(StandardUser)  
# Now PydanticUser is a Pydantic dataclass with validation capabilities, lets test it out

try:
    user = PydanticUser(id=1, name="Bob", signup_ts="2024-01-01T12:00:00", friends=[5, 6, 7])
    print("Pydantic User created successfully:", user)
except ValidationError as e:
    print("Validation Error:", e)