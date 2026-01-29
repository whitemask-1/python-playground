#Object Oriented Programming is a programming style in which devs treat everything like a real world object
#OOP helps to structure code in a way that is modular, reusable, and easier to maintain
#A class is like a blueprint for creating objects
#Every object created from a class is called an instance of that class and has attributes that define data and methods that define behavior

#OOP has four key principles to help you organize and manage code effectively:

#1. Encapsulation - Bundling data and methods that operate on that data within a single unit (class)
#2. Abstraction - Hiding complex implementation details and exposing only the necessary parts
#3. Inheritance - Creating new classes based on existing classes to promote code reuse
#4. Polymorphism - Allowing objects of different classes to be treated as objects of a common superclass, enabling a single interface to represent different underlying forms (data types)

#With encapsulation, you can hide the internal state of the object behind a set of public methods and attributes that act like doors to access and modify the data
#This helps to protect the integrity of the data and prevents unintended interference from outside code
#For Example if you wanted to track a wallet balance using encapsulation you could do something like this:
class Wallet:
    def __init__(self, balance):
        self.__balance = balance  # Private attribute to store wallet balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount  # Add amount to balance
            print(f"Deposited: ${amount:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount  # Subtract amount from balance
            print(f"Withdrew: ${amount:.2f}")
        else:
            print("Insufficient funds or invalid withdrawal amount.")

    def get_balance(self):
        return self.__balance  # Public method to access the balance

#By convention, attributes with a single underscore (_) are considered protected, while those with a double underscore (__) are considered private
#This is because while attributes with a single underscore shouldnt be accessed directly from outside the class, they can still be accessed if needed
#Attributes with a double underscore are name-mangled to make it harder to access them directly from outside the class

account = Wallet(100)
account.deposit(50)
account.withdraw(30)
print(f"Current Balance: ${account.get_balance():.2f}")
#Output:
#Deposited: $50.00
#Withdrew: $30.00
#Current Balance: $120.00

#You can also define a private __validate methods to check if every deposit or withdrawal is a valid amount before modifying the balance

class SecureWallet:
    def __init__(self, balance):
        self.__balance = balance  # Private attribute to store wallet balance

    def __validate(self, amount):
        """Private method to validate transaction amounts."""
        return isinstance(amount, (int, float)) and amount > 0

    def deposit(self, amount):
        if self.__validate(amount):
            self.__balance += amount  # Add amount to balance
            print(f"Deposited: ${amount:.2f}")
        else:
            print("Deposit amount must be a positive number.")

    def withdraw(self, amount):
        if self.__validate(amount) and amount <= self.__balance:
            self.__balance -= amount  # Subtract amount from balance
            print(f"Withdrew: ${amount:.2f}")
        else:
            print("Insufficient funds or invalid withdrawal amount.")

    def get_balance(self):
        return self.__balance  # Public method to access the balance
    
secure_account = SecureWallet(200)
secure_account.deposit(75)
secure_account.withdraw(50)
print(f"Current Balance: ${secure_account.get_balance():.2f}")
#Output:
#Deposited: $75.00
#Withdrew: $50.00
#Current Balance: $225.00

#Validate:
secure_account.deposit(-20)  # Invalid deposit
secure_account.withdraw(500)  # Insufficient funds
#Output:
#Deposit amount must be a positive number.
#Insufficient funds or invalid withdrawal amount.

#The __validate method is private and cant be accessed from outside the SecureWallet class
#But it runs behind the scenes in the deposit and withdraw methods to ensure that only valid amounts are processed

