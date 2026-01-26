#Libraries are like a toolbox for developers that contain pre-written code to perform common tasks.
#Modules are individual files containing Python code that can define functions, classes, and variables.
#A library is a collection of modules bundled together to provide a wide range of functionalities.
#You can use libraries and modules to save time and effort by reusing existing code instead of

#To access a module or library in your Python code, you typically use the import statement.
#For example, to use the math module, you would write:
import math

#Then to call a method from the math module, you would use the dot notation:
result = math.sqrt(16)  # This calls the sqrt function from the math module
print("Square root of 16 is:", result)

#If you need to import the module with a different name (alias), you can use the as keyword:
import math as mathlib
result_alias = mathlib.factorial(5)  # This calls the factorial function from the math module
print("Factorial of 5 is:", result_alias) 

#You can also import specific functions or classes from a module using the from keyword:
from math import pow, pi
power_result = pow(2, 3)  # This calls the pow function directly
print("2 raised to the power of 3 is:", power_result)
print("Value of pi is:", pi)
#This way, you can use pow() and pi directly without prefixing them with math.

#You can also assign aliases to these names:
from math import sqrt as square_root
sqrt_result = square_root(25)
print("Square root of 25 using alias is:", sqrt_result)

#We can also use * to import everything from a module, but it's generally not recommended as it can lead to name conflicts.
#from math import *
#print("Cosine of 0 is:", cos(0))  # Directly using cos()

#Some popular built-in libraries in Python include:
#math - for mathematical functions
#datetime - for manipulating dates and times
#os - for interacting with the operating system
#sys - for system-specific parameters and functions
#random - for generating random numbers
#json - for working with JSON data

#Now that you know how to import and use libraries and modules, you should also know about this idiom:
if __name__ == "__main__":
    # This block will only execute if the script is run directly, not when imported as a module
    print("This script is being run directly.")

#This is useful for testing code in a module without executing it when the module is imported elsewhere.
#You can create your own modules by simply saving your Python code in a .py file and importing it in other scripts.
#For example, if you have a file named mymodule.py with some functions, you can import it using:
# import mymodule
#And then use its functions like:
# mymodule.my_function()