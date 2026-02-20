# Lets explore Pydantic's BaseModel for data validation and settings management
import datetime
from typing import Any
from pydantic import BaseModel, Field, ConfigDict

# Define a Pydantic model using BaseModel
class User(BaseModel):
    id: int = Field(..., title="ID", description="The unique identifier for the user")
    name: str = Field(..., title="Name", description="The name of the user")
    signup_ts: datetime.datetime | None = Field(None, title="Signup Timestamp", description="The timestamp when the user signed up")
    friends: list[int] = Field([], title="Friends", description="List of friend IDs")

    model_config = ConfigDict(extra="allow")  # Allow extra fields not defined in the model

#    __class_vars__ = { # __class_vars__ is a special attribute that holds class variable definitions for Pydantic models
#        'id': int,
#        'name': str,
#        'signup_ts': datetime.datetime.now(),
#        'friends': list[int]
#    }

#    __private_attributes__ = { # __private_attributes__ is a special attribute that holds private attribute definitions for Pydantic models
#        '_internal_id': int
#    }

#    __signature__ = ( # __signature__ is a special attribute that holds the signature of the model's __init__ method
#        'id', # Notice signatures uses a tuple of strings to define the order of parameters
#        'name',
#        'signup_ts',
#        'friends'
#    )

#    __pydantic_complete__ = True # __pydantic_complete__ indicates whether the model is fully defined or there are still undefined fields

#    __pydantic_core_schema__ = { # __pydantic_core_schema__ holds the core schema definition for the model
#        'type': 'model',
#        'fields': {
#            'id': {'type': 'int'},
#            'name': {'type': 'str'},
#            'signup_ts': {'type': 'datetime', 'nullable': True},
#            'friends': {'type': 'list', 'items': {'type': 'int'}}
#        }
#    }

#    __pydantic_custom_init__ = False # __pydantic_custom_init__ indicates whether the model has a custom __init__ method which can be used for additional initialization logic

#   __pydantic_decorators__ = [] # __pydantic_decorators__ holds any decorators applied to the model, Metadata containing the decorators defined on the model. This replaces Model.__validators__ and Model.__root_validators__ from Pydantic V1.

#    __pydantic_generic_metadata__ = None # Metadata for generic models; contains data used for a similar purpose to args, origin, parameters in typing-module generics. May eventually be replaced by these.

#    __pydantic_parent_namespace__ = None # __pydantic_parent_namespace__ holds the parent namespace for the model, used for automatic rebuilding of models

#    __pydantic_post_init__ = None # __pydantic_post_init__ holds a reference to a post-initialization method for the model, allowing for additional setup after the model is created

#    __pydantic_root_model__ = False # __pydantic_root_model__ indicates whether the model is a root model, which can be used for models that represent a single value rather than a structured object

#    __pydantic_serializer__ = None # __pydantic_serializer__ holds a reference to a custom serializer for the model, allowing for custom serialization logic when converting the model to JSON or other formats, which can be useful for complex data types or specific formatting requirements

#    __pydantic_validator__ = None # __pydantic_validator__ holds a reference to a custom validator for the model, allowing for custom validation logic when creating or updating the model instance

#    __pydantic_fields__ = { # __pydantic_fields__ holds the field definitions for the model
#        'id': int, # This is an alternative way to doing it with __class_vars__
#        'name': str,
#        'signup_ts': datetime.datetime.now(),
#        'friends': list[int]
#    }

#    __pydantic_computed_fields__ = {} # __pydantic_computed_fields__ holds computed field definitions for the model, allowing for fields that are derived from other fields or calculations

#    __pydantic_extra__ = {} # __pydantic_extra__ holds any extra metadata or configuration for the model, allowing for additional customization beyond the standard Pydantic features

#    __pydantic_fields_set__ = {'id', 'name', 'signup_ts', 'friends'} # __pydantic_fields_set__ holds the set of field names for the model explicitly set during instantiation, allowing for easy access to the fields defined in the model

#    __pydantic_private__ = {'_internal_id': int} # __pydantic_private__ holds private attribute definitions for the model, similar to __private_attributes__   

#    model_config: ConfigDict = ConfigDict() # model_config holds configuration settings for the model, allowing for customization of behavior such as validation, serialization, and more
    # class attribute to configure the model using a dictionary settings approach ex. title : str | None

#    def model_fields() -> dict[str, Any]: # a method to mapp field names to their respective FieldInfo
#        return { # model_fields holds the field definitions for the model, similar to __pydantic_fields__
#            'id': Field(..., title="ID", description="The unique identifier for the user"),
#            'name': Field(..., title="Name", description="The name of the user"),
#            'signup_ts': Field(None, title="Signup Timestamp", description="The timestamp when the user signed up"),
#            'friends': Field([], title="Friends", description="List of friend IDs")
#       }
    
#    def model_computed_fields() -> dict[str, Any]: # a method to map computed field names to their respective definitions
#        pass # model_computed_fields holds computed field definitions for the model, similar to __pydantic_computed_fields__
    
# Example usage of the User model
user = User(
    id=1,
    name="Alice",
    signup_ts=datetime.datetime.now(),
    friends=[2, 3, 4]
)
print(user)

# model_extra is what allows us to grab undefined fields when creating a model instance and still be able to access them later.
extra_user = User(
    id=2,
    name="Bob",
    signup_ts=datetime.datetime.now(),
    friends=[5, 6],
    extra_field="This is an extra field"
)

print(extra_user)
print(extra_user.model_extra)  # Accessing the extra field

set_of_fields = user.model_fields_set
print(set_of_fields)  # Output: {'id', 'name', 'signup_ts', 'friends'}