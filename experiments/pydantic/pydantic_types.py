# Pydantics .type module provides a collection of custom datatypes that extend the functionality of standard Python types.
# These types include enhanced versions of strings, numbers, dates, and more, with built-in validation and parsing capabilities.
from pydantic import BaseModel
from pydantic.types import PositiveInt, NegativeInt, SocketPath, StrictBool, Strict, SecretStr
from datetime import date, datetime
from typing import Annotated

class CustomTypesModel(BaseModel):
    positive_integer: PositiveInt
    negative_integer: NegativeInt
    socket_path: SocketPath | None
    strict_boolean: StrictBool
    strict_string: Annotated[str, Strict]
    secret_string: SecretStr
    birth_date: date
    appointment_datetime: datetime

# Example usage
data = {
    "positive_integer": 10,
    "negative_integer": -5,
    "socket_path": None,
    "strict_boolean": True,
    "strict_string": "This is a strict string",
    "secret_string": "my_secret_password",
    "birth_date": "1990-01-01",
    "appointment_datetime": "2024-06-15T14:30:00"
}

model = CustomTypesModel(**data)
print(model)