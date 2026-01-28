#Classes are buuild to define shared behavior and attributes for objects
#They are blueprints for creating objects

#To create a class, use the class keyword followed by the class name and a colon
class Dog:
    #Then within the class you can add an initializer along with any attributes and methods
    def __init__(self, name, age):
        self.name = name  # Attribute to store the dog's name
        self.age = age    # Attribute to store the dog's age

    def bark(self):
        return f"{self.name} says Woof!"  # Method for the dog to bark
    
#def __init__ is the special method automatically called when a new object is created
#It initializes the attributes of the objects that will be created with the class

#self refers to the instance of the class being created
#As the first parameter of any method in the class, it allows access to the instance's attributes and other methods

#With the class defined, you can create objects (instances) of that class
my_dog = Dog("Buddy", 3)  # Creating an instance of Dog with name "Buddy" and age 3
print(my_dog.name)      # Output: Buddy
print(my_dog.age)       # Output: 3
print(my_dog.bark())      # Output: Buddy says Woof!