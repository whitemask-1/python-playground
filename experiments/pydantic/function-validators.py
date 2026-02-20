# What are function validators in Pydantic and how do you use them?
# Function validators are methods that allow you to add custom validation logic to your Pydantic models.
# They are defined using the @model_validator decorator and can be used to validate individual fields or the entire model after instantiation/initial validation.

from pydantic import BaseModel, model_validator, ValidationError, ConfigDict
from datetime import datetime

class User(BaseModel):
    id: int
    name: str
    signup_ts: datetime | None = None
    friends: list[int] = []

    model_config = ConfigDict(
        validate_assignment=True,  # Validate data on assignment to attributes
    )

    @model_validator(mode='before') #This function validator runs before standard validation as can be seen with the mode = "before" parameter
    def check_name_not_empty(cls, values): # It checks that the name field isnt empty and if it is then it will raise a validation error
        name = values.get('name')
        if not name or not name.strip():
            raise ValidationError('Name must not be empty')
        return values

    @model_validator(mode='after') #This function validator runs after standard validation as can be seen with the mode = "after" parameter
    def check_signup_ts_in_past(cls, model): # It checks that the signup_ts field is in the past and if it is not then it will raise a validation error
        if model.signup_ts and model.signup_ts > datetime.now():
            raise ValidationError('signup_ts must be in the past')
        return model
    
# Example usage
try: # This will raise a validation error because the name is empty
    user = User(id=1, name="  ", signup_ts="2025-01-01T12:00:00", friends=[2, 3, 4])
except ValidationError as e:
    print("Validation Error:", e)

try: # This will raise a validation error because the signup_ts is in the future
    user = User(id=1, name="John Doe", signup_ts="2027-01-01T12:00:00", friends=[2, 3, 4])
    print("User created successfully:", user)
except ValidationError as e:
    print("Validation Error:", e)

# This will succeed because both validations pass
user = User(id=1, name="Jane Doe", signup_ts="2020-01-01T12:00:00", friends=[2, 3, 4])
print("User created successfully:", user)