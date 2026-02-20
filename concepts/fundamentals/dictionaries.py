#Dictionaries are built-in data structures that store collections of key-value pairs.
#They are also sometimes referred to as associative arrays or hash maps in other programming languages.
#Dictionaries are mutable, meaning you can change their contents after creation.
#Dictionaries are defined using curly braces {} with key-value pairs separated by commas.

#Basic Syntax:
#my_dict = {key1: value1, key2: value2, ...}

#Example 1: Creating a simple dictionary
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
#When you think of a dictionary, think of it like a real-world dictionary where you look up a word (key) to find its definition (value).
print("Person Dictionary:", person)
print(type(person))  # Outputs: <class 'dict'>

#Keys must be unique and immutable (e.g., strings, numbers, or tuples), while values can be of any data type and can be duplicated.

cube = {
    (0,0,0): "Point A",
    (1,0,0): "Point B",
    (0,1,0): "Point C",
    (0,0,1): "Point D",
    (1,1,1): "Point E",
    (1,1,0): "Point F",
    (1,0,1): "Point G",
    (0,1,1): "Point H"
}

#You can access dictionary values using their keys.
name = person["name"]  # 'Alice'
age = person["age"]    # 30
print("Name:", name)
print("Age:", age)

#Another alternative would be using the dict() constructor to create dictionaries.
fruits = dict(apple=1, banana=2, cherry=3)
print("Fruits Dictionary:", fruits)
print(type(fruits))  # Outputs: <class 'dict'>

#Notice difference in syntax when using the dict() constructor, keys are provided as keyword arguments without quotes.
#You can also create dictionaries from a list of tuples using the dict() constructor.
pizza = dict([("size", "large"), ("crust", "thin"), ("toppings", ["pepperoni", "mushrooms"])])
print("Pizza Dictionary:", pizza)
print(type(pizza))  # Outputs: <class 'dict'>

#Dictionaries support various methods for adding, removing, and modifying key-value pairs.
person["email"] = "alice@example.com"  # Adds a new key-value pair
print("After adding email:", person)
person["age"] = 31  # Modifies the value for the key 'age'
print("After modifying age:", person)
del person["city"]  # Removes the key-value pair with key 'city'
print("After deleting city:", person)
person.pop("name")  # Removes the key-value pair with key 'name' and returns
print("After popping name:", person)

#You can use the keys(), values(), and items() methods to get views of the dictionary's keys, values, and key-value pairs respectively.
keys = person.keys()
values = person.values()
items = person.items()
print("Keys:", keys)
print("Values:", values)
print("Items:", items)

#The get() method is used to retrieve the value for a given key, returning None (or a specified default value) if the key does not exist.
email = person.get("email")  # 'alice@example.com'
phone = person.get("phone", "Not Available")  # 'Not Available' since 'phone' key doesn't exist, second argument is default value
print("Email:", email)
print("Phone:", phone)

#popitem() method removes and returns an arbitrary key-value pair from the dictionary.
removed_item = person.popitem()
print("Removed item:", removed_item)
print("After popitem:", person)

#To check if a key exists in a dictionary, you can use the 'in' keyword.
if "age" in person:
    print("Age is in the person dictionary.")

#Dictionaries can also be nested, meaning you can have dictionaries within dictionaries.
student = {
    "name": "Bob",
    "grades": {
        "math": 90,
        "science": 85,
        "history": 88
    }
}
print("Student Dictionary:", student)
print("Math Grade:", student["grades"]["math"])  # Accessing nested dictionary value

#The update() method is used to update a dictionary with key-value pairs from another dictionary or an iterable of key-value pairs.
student.update({"age": 20, "city": "Los Angeles"})
print("After update:", student)

#A view object returned by keys(), values(), or items() methods reflects changes made to the dictionary.