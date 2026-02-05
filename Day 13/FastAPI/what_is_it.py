import fastapi
app = fastapi.FastAPI()

# FastAPI is a modern, fast, webframework for building APIs with Python based on standard Python type hints.
# It allows for automatic generation of interactive API documentation, validation of request and response data through Pydantic models,
# and is built on top of Starlette for web parts which provides a tool for building high-performance asynchronous web applications.

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}") # @app.get defines a GET endpoint, a GET endpoint is used to retrieve data from the server which in this case is an item by its ID.
async def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

# The async calls in FastAPI allow for handling multiple requests concurrently, making it suitable for high-performance applications.
# Note that if you use async functions, you should ensure that any I/O operations within those functions are also asynchronous to fully benefit from the async capabilities.

#You can easily run this FastAPI application using Uvicorn, an ASGI server, with the command:
# fastapi dev {file_name}:app --reload
# in this case, it would be:
# fastapi dev what_is_it:app --reload

import typing

def newfunc(x: int | float) -> str: # This function uses the union type hint for parameter x and then a type hint for the return type as str.
    return f"The computed value is {x * 2}" # This means I dont have to convert the return value to a string, Python will do it for me.

result = newfunc(5)

def optionalfunc(name: str, age: typing.Optional[int] = None) -> str: # in the typing module, Optional is just shorthand for the Union type hint with None. Union[X, None] is equivalent to Optional[X].
    if age:
        return f"{name} is {age} years old."
    else:
        return f"{name}'s age is unknown."
    
result_optional = optionalfunc("Alice")

print(result)
print(result_optional)

# We can also use type hints for classes and their attributes.
class Person:
    def __init__(self, name: str, age: typing.Optional[int | str] = None):
        self.name: str = name
        if age is not None:
            self.age: int | str = age
        else:
            self.age: str = "unknown"

def person_info(person: Person) -> str:
    if person.age == "unknown":
        return f"{person.name}'s age is {person.age}."
    return f"{person.name} is {person.age} years old."

person1 = Person("Bob", 30)
person2 = Person("Charlie")
info1 = person_info(person1)
info2 = person_info(person2)

print(info1)
print(info2)