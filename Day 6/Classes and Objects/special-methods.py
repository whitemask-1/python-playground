#Special methods aka "magic methods" or "dunder methods" in Python are predefined methods that you can define to add special behavior to your classes
#They are always surrounded by double underscores (__) and allow you to customize how your objects behave

#You have probably already used some special methods without realizing it
#For example, the __init__ method is a special method that is called when an object is created from a class
#It is used to initialize the attributes of the object
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

point = Point(2, 3)
print(f"Point coordinates: ({point.x}, {point.y})")  # Output:

#3+4 calls the __add__ special method of the integer class
result = (3).__add__(4)
print(result)  # Output: 7

#There is also a __str__ special method that defines how an object is represented as a string
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}, {self.age} years old"
    
#You dont need to call special methods directly
#Instead, you can use built-in functions or operators that internally call these methods

person = Person("Alice", 30)
print(person)  # Output: Alice, 30 years old

#The main usecase of special methods is to customize the behavior of your classes
#This is because Python won't know how to handle certain operations on your custom objects unless you define the appropriate special methods
#For example, if you want to add two Point objects together, you can define the __add__ method
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"({self.x}, {self.y})"
    
point1 = Point(2, 3)
point2 = Point(4, 5)
result = point1 + point2  # This calls point1.__add__(point2)
print(result)  # Output: (6, 8)

#Using __str__ method to print the Point object nicely
print(str(result))  # Output: (6, 8)

#Full list of magic methods: https://docs.python.org/3/reference/datamodel.html#special-method-names
#Magic methods essentially serve to allow you to define how built in functions and operators behave with your custom classes