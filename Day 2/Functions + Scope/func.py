#Functions are reusable pieces of code that perform a specific task.
#They help in organizing code, improving readability, and reducing redundancy.
#Defining a function using the def keyword
def greet(name):
    """This function greets the person whose name is passed as an argument."""
    print(f"Hello, {name}!")
#Calling the function
greet("Alice")
greet("Bob")

def hello():
    """This function prints a simple hello message."""
    print("Hello, World!")
hello()

def add(a, b):
    """This function returns the sum of two numbers."""
    return a + b #Functions also use a special keyword 'return' to send back a result to the caller.
result = add(5, 3)# If you dont use return, the function will return None by default.
result2 = add(-1, 10)
print(result)
print(result2)
print(result + result2)

#Functions can call themselves recursively to solve problems.
def factorial(n):
    """This function returns the factorial of a given number n."""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
print(factorial(5))  # Outputs: 120
print(factorial(0))  # Outputs: 1

#Functions can have default parameter values.
def power(base, exponent=2):
    """This function returns the base raised to the power of exponent."""
    return base ** exponent
print(power(3))       # Outputs: 9 (3^2)
print(power(2, 3))    # Outputs: 8 (2^3)

#Functions can accept a variable number of arguments using *args and **kwargs.
def variable_args(*args, **kwargs):
    """This function demonstrates variable number of arguments."""
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)
variable_args(1, 2, 3, name="Alice", age=30)

#Lambda functions are small anonymous functions defined using the lambda keyword.
square = lambda x: x ** 2
print(square(5))  # Outputs: 25 

#Lambda functions are often used for short, throwaway functions, especially as arguments to higher-order functions like map(), filter(), and reduce().
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers)  # Outputs: [1, 4, 9, 16, 25]
#list and map are defined in-built functions in python
#Understanding functions is crucial for writing modular and maintainable code in Python.
#They allow you to encapsulate logic, reuse code, and create more complex programs efficiently.
