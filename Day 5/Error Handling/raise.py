#The raise statement allows you to trigger exceptions intentionally in your code
#It gives you control over when and how errors are generated, enabling you to create custom error conditions and enfore specific program behavior
#The raise statement is used explicitly to throw an error or exceptional condition that has occurred at any point in your code

#The raise statement can be used in several ways to trigger exceptions
#The most basic form is to raise built-in exceptions or create custom exceptions
#Basic Example:
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")  # Raising a built-in exception
    return a / b

try:
    result = divide(10, 0)
except ValueError as ve:
    print(f"Error Caught: {ve}")
#In this example, if the divisor b is zero, a ValueError is raised with a custom error message
#The exception is then caught in the try-except block, allowing for graceful error handling
#This is useful to put error messages into natural language for users to understand what went wrong

#The raise statement can also be used to re-raise exceptions that have been caught
#This is useful when you want to handle an exception partially and then propagate it further up the call stack
def process_data(data):
    try:
        # Simulate processing that may raise an exception
        result = 10 / data
        return result
    except ZeroDivisionError as zde:
        print("Caught a division by zero error, re-raising it.")
        raise  # Re-raise the caught exception 

try:
    process_data(0)
except ZeroDivisionError as zde:
    print(f"Error Re-Caught: {zde}")
#In this example, when a ZeroDivisionError is caught, a message is printed, and the same exception is re-raised using raise without any arguments
#By re-raise we mean we throw the same exception again to be handled elsewhere
#Far easier to understand if you think about it as a try call within the function and another try call outside the function
#then the raise statement at the end of the function "raises" the exception to the outer try-except block
#This allows the exception to be handled again in the outer try-except block

#What if we want to catch some of the exceptions and pool the rest into a general exception handler?
def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError as fnfe: # Catch specific exception
        print(f"File not found: {fnfe}")
    except Exception as e: # Catch all other exceptions
        print("An unexpected error occurred, re-raising the exception.")
        raise  # Re-raise any other unexpected exceptions

try:
    read_file("non_existent_file.txt")
except Exception as e:
    print(f"Error Re-Caught in outer block: {e}")
#In this example, we catch a specific FileNotFoundError and handle it by printing a message
#For any other unexpected exceptions, we print a general message and re-raise the exception
#This allows us to handle known exceptions while still allowing unknown exceptions to be propagated for further handling
#Note that the FileNotFoundError isnt raised again, and therefore doesnt appear in the outer try-except block
#Therefore we can run the function without worrying about that specific error crashing our program
#But any other unexpected error will be raised again and caught in the outer block

#You can also create and raise custom exceptions using the raise statement by defining your own exception classes
class InsufficientFundsError(Exception):
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(f"Insufficient funds: Available balance is {balance}, attempted to withdraw {amount}")

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError(balance, amount)  # Raising a custom exception
    return balance - amount

try:
    withdraw(100, 150)
except InsufficientFundsError as ife:
    print(f"Insufficient Funds: Tried to withdraw {ife.amount} with balance {ife.balance}")
#In this example, we define a custom exception InsufficientFundsError that inherits from the built-in Exception class
#When the withdraw function is called with an amount greater than the balance, the custom exception is raised
#The exception is then caught in the try-except block, allowing for specific handling of the custom error condition

#The raise statement can also be used with the from keyword to chain exceptions together
#This is useful when you want to raise a new exception while preserving the context of the original exception
def parse_integer(value):
    try:
        return int(value)
    except ValueError as ve:
        raise ValueError("Failed to parse integer from input.") from ve  # Chaining exceptions
    except FileNotFoundError as fnfe:
        raise FileNotFoundError("File not found during parsing.") from fnfe
#In this example, if a ValueError occurs while converting the input to an integer, a new ValueError is raised with a custom message
#The original ValueError is chained to the new exception using the from keyword, preserving the context

try:
    parse_integer("abc")
except ValueError as ve:
    print(f"Chained Error Caught: {ve}")
    print(f"Original Cause: {ve.__cause__}")
#When the chained exception is caught, both the new exception message and the original cause can be accessed
#This provides more context about the error and helps in debugging

#You can also raise exceptions conditionally based on specific criteria in your code using assert statements which is essentially shorthand for raising exceptions with AssertionError
def check_positive(number):
    assert number > 0, "Number must be positive."  # Raises AssertionError if condition is False
    return True

try:
    check_positive(-5)
except AssertionError as ae:
    print(f"Assertion Error Caught: {ae}")
#In this example, if the number is not positive, an AssertionError is raised with a custom message
#The exception is then caught in the try-except block, allowing for handling of the assertion failure

#Raise keyword is a powerful tool that must be understood well, however it is not the most straightforward concept in Python
#This Youtube video explains it well for a base understanding to build on: https://www.youtube.com/watch?v=V_NXT2-QIlE

