#Polymophism allos us to use an interface to interact with many objects of the same kind
#For Example we can define a common interface for different shapes like Circle, Square, and Triangle
#Each shape class will implement a method to calculate its area
class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement this method")
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        import math
        return math.pi * (self.radius ** 2)
    
class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side
    
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height
    
#Now we can create a list of different shapes and calculate their areas using the same interface
shapes = [Circle(5), Square(4), Triangle(3, 6)]
for shape in shapes:
    print(f"Area: {shape.area()}") #Polymorphic call to area method

#Output:
#Area: 78.53981633974483
#Area: 16
#Area: 9.0

#This demonstrates polymorphism as we can treat different shape objects uniformly through the common Shape interface

#Heres another example, with instances and an attribute
class Twitter:
    def __init__(self, content):
        self.content = content

    def post(self):
        return f"🐦 Tweet: '{self.content}' (280 chars max)"
    
class Instagram:
    def __init__(self, content):
        self.content = content

    def post(self):
        return f"📸 Instagram Post: '{self.content}' + ✨ filters"
class LinkedIn:
    def __init__(self, content):
        self.content = content

    def post(self):
        return f"💼 LinkedIn Article: '{self.content}' (Professional Mode)"
    
# Function demonstrating polymorphism
def start(social_media):
    print(social_media.post())  # Calls .post() on any object

# Instances
tweet = Twitter('Just learned Python polymorphism!')
photo = Instagram('Sunset vibes 🌅')
article = LinkedIn('Why OOP matters in 2024')

# The polymorphic calls - same function, different outputs
start(tweet) # 🐦 Tweet: 'Just learned Python polymorphism!' (280 chars max)
start(photo) # 📸 Instagram Post: 'Sunset vibes 🌅' + ✨ filters
start(article) # 💼 LinkedIn Article: 'Why OOP matters in 2024' (Professional Mode)

#There is also inheritance-based polymorphism where subclasses inherit from a common superclass and override methods to provide specific implementations
#This allows objects of the subclasses to be treated as objects of the superclass while still exhibiting their unique behaviors
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound"
    
class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"
    
class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"
    
#Function demonstrating polymorphism through inheritance
def animal_sound(animal):
    print(animal.speak())  # Calls .speak() on any Animal object

#Instances
dog = Dog("Buddy")
cat = Cat("Whiskers")

animal_sound(dog)  # Buddy says Woof!
animal_sound(cat)  # Whiskers says Meow!