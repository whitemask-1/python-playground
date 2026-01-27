#Exception handling is the process of catching and managing errors that occur during the execution of a program
#It allows developers to gracefully handle unexpected situations without crashing the program

#Python provides the try, except, else, and finally blocks to gracefully handle exceptions
#Basic Structure:
#try:
#    Code that may raise an exception
#    pass
#except SomeException as e:
#    Code to handle the exception
#    pass

#Basic Example:
try:
    result = 10 / 0  # This will raise a ZeroDivisionError
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

#Example using else and finally:
try:
    file = open('example.txt', 'r')
except FileNotFoundError:
    print("Error: File not found.")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("File closed.")
#This code block attempts to open and read a file, handling the case where the file does not exist
#The else block runs if no exceptions occur, and the finally block always runs to ensure the file is closed
#Note: with statement is preferred for file operations to handle closing automatically

#You can also catch multiple exceptions:
try:
    value = int(input("Enter a number: "))
    result = 10 / value
except ValueError:
    print("Error: Invalid input. Please enter a valid integer.")
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
#This code handles both invalid input and division by zero errors separately

#This can also be useful for handling several possible edge case errors within a function using custom exceptions
#Custom Exceptions:
class CustomError(Exception):
    """A custom exception type for specific error handling."""
    pass

def risky_function(param):
    if param < 0:
        raise CustomError("Parameter cannot be negative.")
    return param * 2
try:
    risky_function(-5)
except CustomError as ce:
    print(f"Custom Error Caught: {ce}")
#Raising custom exceptions allows you to define specific error conditions relevant to your application logic