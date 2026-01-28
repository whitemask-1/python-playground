#Attributes are variables that belong to an object, therefore they hold data about the object
#There are two kinds of attributes:

#Instance Attributes - Attributes that are specific to an instance of a class
#Class Attributes - Attributes that are shared across all instances of a class
#For Example:
class Car:
    #Class Attribute
    wheels = 4  # All cars have 4 wheels

    def __init__(self, make, model):
        #Instance Attributes
        self.make = make  # Specific to each car instance
        self.model = model  # Specific to each car instance

    def display_info(self):
        return f"{self.make} {self.model} with {Car.wheels} wheels"
    
#Creating instances/objects of the Car class
car1 = Car("Toyota", "Camry")
car2 = Car("Honda", "Civic")

print(car1.display_info())  # Output: Toyota Camry with 4 wheels
print(car2.display_info())  # Output: Honda Civic with 4 wheels

#Note that you can access class attributes directly from the class itself using Car.wheels
#But to access instance attributes you need to use the instance like car1.make or car2.model

#Methods are functions that are defined within a class and operate on the data contained in the class
#They define the behavior of the objects created from the class
#Methods can manipulate instance attributes and perform operations related to the object
#For Example:
class Circle:
    def __init__(self, radius):
        self.radius = radius  # Instance attribute

    def area(self):
        import math
        return math.pi * (self.radius ** 2)  # Method to calculate area

    def circumference(self):
        import math
        return 2 * math.pi * self.radius  # Method to calculate circumference
    
#Creating an instance of Circle
circle = Circle(5)
print(f"Area: {circle.area()}")  # Output: Area: 78.53981633974483
print(f"Circumference: {circle.circumference()}")  # Output: Circumference: 31.41592653589793