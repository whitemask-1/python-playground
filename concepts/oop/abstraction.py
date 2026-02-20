#Abstraction is the process of hiding complex implementation details and exposing only the necessary parts of an object or system
#Think of it as focusing on what something does rather than how it does it

#Abstraction is not limited to Python OOP but is a general programming concept
#In a single sentence: Abstraction works to provide you a simplified interface to interact with a complex system

#As for how Python implements abstraction, it does so through the abc (Abstract Base Classes) module
#This module provides the ABC class and the @abstractmethod decorator to define abstract base classes and methods
from abc import ABC, abstractmethod

#An abstract class is a class that cannot be instantiated directly
#It serves as a blueprint for other classes and can contain abstract methods that must be implemented by any subclass
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass  # Abstract method that must be implemented by subclasses

#Concrete subclass implementing the abstract method
class Dog(Animal):
    def make_sound(self):
        return "Woof!"
    
class Cat(Animal):
    def make_sound(self):
        return "Meow!"
    
#Subclasses of an abstract class must implement all abstract methods
#Otherwise, they will also be considered abstract and cannot be instantiated
#For Example, the following class would raise an error if we tried to create an instance of it
class Fish(Animal):
    pass  # Does not implement make_sound, so Fish is still abstract

#Creating instances of the concrete subclasses
dog = Dog()
cat = Cat()

print(dog.make_sound())  # Output: Woof!
print(cat.make_sound())  # Output: Meow!

#A more complex example of abstraction could involve a payment processing system
class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass  # Abstract method to process payment

class PayPalProcessor(PaymentProcessor):
    def process_payment(self, amount):
        return f"Processing PayPal payment of ${amount:.2f}"
    
class StripeProcessor(PaymentProcessor):
    def process_payment(self, amount):
        return f"Processing Stripe payment of ${amount:.2f}"
    
#Function to demonstrate abstraction in payment processing
def make_payment(processor: PaymentProcessor, amount):
    print(processor.process_payment(amount))

#Using different payment processors interchangeably
paypal = PayPalProcessor()
stripe = StripeProcessor()

make_payment(paypal, 100.00)  # Output: Processing PayPal payment of $100.00
make_payment(stripe, 150.50)  # Output: Processing Stripe payment of $150.50

