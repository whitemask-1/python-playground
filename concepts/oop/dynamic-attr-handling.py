#Sometimes you may no know which attributes you need until your program is running
#In such cases you can use dynamic attribute handling to access, modify, check, or delete attributes using their names as variables and not as fixed names in your code
#This gives your program flexibility to work with attributes that are determined at runtime

#Python gives you four built-in functions to handle attributes dynamically:
#getattr() - To get the value of an attribute by name , Basic syntax: getattr(object, 'attribute_name', default_value)
#setattr() - To set the value of an attribute by name , Basic syntax: setattr(object, 'attribute_name', value)
#hasattr() - To check if an attribute exists by name , Basic syntax: hasattr(object, 'attribute_name')
#delattr() - To delete an attribute by name , Basic syntax: delattr(object, 'attribute_name')

#Example class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

#Creating an instance of Person
person = Person("Alice", 30)

#Using getattr to access attributes dynamically
name = getattr(person, 'name')  # Equivalent to person.name
age = getattr(person, 'age')    # Equivalent to person.age
print(f"Name: {name}, Age: {age}")  # Output: Name: Alice, Age: 30

#Note that if the attribute does not exist, getattr will raise an AttributeError
#You can provide a default value as a third argument to avoid the error
nickname = getattr(person, 'nickname', 'No nickname')  # Default value if attribute not found
print(f"Nickname: {nickname}")  # Output: Nickname: No nickname

#If you want to look through all the attributes an object has, you can use the built in dir() function
attributes = dir(person)
print(f"Attributes of person: {attributes}")
#Output will include 'name', 'age', and other default attributes/methods

#The vars() function can also be used to get the __dict__ attribute of an object which is a dictionary of all its attributes
attributes_dict = vars(person)
print(f"Attributes Dictionary: {attributes_dict}")
#Output: Attributes Dictionary: {'name': 'Alice', 'age': 31}

#Using setattr to modify attributes dynamically
setattr(person, 'age', 31)  # Equivalent to person.age = 31
new_age = getattr(person, 'age')
print(f"Updated Age: {new_age}")  # Output: Updated Age: 31

#Using hasattr() to check if an attribute exists, before doing something with it
if hasattr(person, 'name'):
    print("Person has a name attribute.")
if hasattr(person, 'nickname'):
    print("Person has a nickname attribute.")
else:
    print("Person does not have a nickname attribute.")
#Output: Person has a name attribute.
#        Person does not have a nickname attribute. 

#Using delattr() to delete an attribute dynamically
delattr(person, 'age')  # Equivalent to del person.age
if not hasattr(person, 'age'):
    print("Age attribute has been deleted.")
else:
    print(f"Age attribute still exists: {getattr(person, 'age')}")
#Output: Age attribute has been deleted.

#Dynamic attribute handling is especially useful in scenarios where attribute names are not known until runtime
#For example, when working with data from external sources like JSON, databases, or user input
#It allows you to write flexible and generic code that can adapt to different attribute names and structures
#However, use dynamic attribute handling judiciously as it can make code harder to read and debug
#Always ensure proper error handling when accessing attributes dynamically to avoid unexpected crashes