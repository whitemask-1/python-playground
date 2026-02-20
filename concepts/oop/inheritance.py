#Inheritance allows a class (child class) to inherit attributes and methods from another class (parent class)
#This promotes code reusability and establishes a hierarchical relationship between classes

#Example of Inheritance
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound"
class Dog(Animal):
    def bark(self):
        return f"{self.name} says Woof!"

class Cat(Animal):
    def  meow(self):
        return f"{self.name} says Meow!"

#Creating instances of Dog and Cat
dog = Dog("Buddy")
cat = Cat("Whiskers")
whale = Animal("Wally")

print(dog.bark())
print(cat.meow())
print(whale.speak())  # This will raise an error since Animal's speak method is not implemented

#If you want to keep the return value of the parent class method while adding extra functionality in the child class, you can use the super() function
class Bird(Animal):
    def speak(self):
        parent_speak = super().speak()  # Call the parent class method
        return f"{self.name} chirps! Also, {parent_speak}"

bird = Bird("Tweety")
print(bird.speak())  # This will not raise an error since Animal's speak method is now implemented

#In this way you can extend or modify the behavior of inherited methods while still retaining the original functionality from the parent class
#You can also create multi-level inheritance where a class inherits from a child class
class Puppy(Dog):
    def weep(self):
        return f"{self.name} is weeping!"
    
puppy = Puppy("Max")
print(puppy.bark())  # Inherited from Dog
print(puppy.weep())  # Defined in Puppy

#Another simple demonstration of multi-level inheritance:
class WalkingAnimal(Animal):
    def walk(self):
        return f"{self.name} is walking."

class SwimmingAnimal(Animal):
    def swim(self):
        return f"{self.name} is swimming."

class Frog(WalkingAnimal, SwimmingAnimal):
    def croak(self):
        return f"{self.name} says Ribbit!"

frog = Frog("Freddy")
print(frog.walk())  # Inherited from WalkingAnimal
print(frog.swim())  # Inherited from SwimmingAnimal
print(frog.croak())  # Defined in Frog

#The easiest way to remember inheritance is that it allows you to build upon existing classes with more specific subclasses
#This helps to keep your code organized and reduces redundancy by reusing code from parent classes
