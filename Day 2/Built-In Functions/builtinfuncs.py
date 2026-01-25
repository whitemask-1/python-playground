#In Python there are a lot of built-in functions that help us perform common tasks easily.
#Let's explore some of the most commonly used built-in functions.
#The print() function is used to display output to the console.
print("Hello, World!")  # Outputs: Hello, World!
#The type() function returns the data type of a variable or value.
print(type(42))          # Outputs: <class 'int'>
print(type(3.14))        # Outputs: <class 'float'>
print(type("Python"))    # Outputs: <class 'str'>
print(type([1, 2, 3]))   # Outputs: <class 'list
#The len() function returns the length of a string, list, tuple, or other iterable.
sample_string = "Hello, Python!"
length = len(sample_string)
#The isinstance() function checks if a variable is of a specific data type and returns True or False.
is_string = isinstance(sample_string, str)  # Returns: True
is_integer = isinstance(sample_string, int)  # Returns: False
print("Length of sample_string:", length)
print("Is sample_string a string?", is_string)
print("Is sample_string an integer?", is_integer)
#The input() function allows you to take user input from the console.
# Uncomment the lines below to test user input functionality
user_name = input("Enter your name: ")
print("Hello, " + user_name + "!")
#The str(), int(), and float() functions are used to convert values between different data types.
num_str = "100"
num_int = int(num_str)      # Converts string to integer
num_float = float(num_str)  # Converts string to float
print("String:", num_str)
print("Converted to Integer:", num_int)
print("Converted to Float:", num_float)
#The round() function rounds a floating-point number to a specified number of decimal places.
original_value = 3.14159
rounded_value = round(original_value, 2)  # Rounds to 2 decimal places
print("Original Value:", original_value)
print("Rounded Value:", rounded_value)

#map() function applies a given function to all items in an iterable (like a list) and returns a map object (which can be converted to a list or other iterables).
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))  # Squares each number
print("Original Numbers:", numbers)
print("Squared Numbers:", squared_numbers)
#list() function converts an iterable (like a string, tuple, or map object) into a list.
string_example = "Python"
char_list = list(string_example)  # Converts string to list of characters
print("String:", string_example)
print("List of Characters:", char_list)
#lambda functions are small anonymous functions defined using the lambda keyword.
#They are often used for short, throwaway functions, especially as arguments to higher-order functions like map(), filter(), and reduce().
add = lambda x, y: x + y
result = add(5, 3)  # Returns: 8

#Can we use a custom function with map() instead of lambda?
def square(x):
    return x ** 2
squared_numbers_custom = list(map(square, numbers))  # Using custom function
print("Squared Numbers using custom function:", squared_numbers_custom)
#These are just a few of the many built-in functions available in Python.
#Exploring and understanding these functions will help you write more efficient and effective Python code!
#Let's dive deeper into some of these functions with examples!
print("Result of add function:", result)
#Let's explore string manipulation using built-in functions and methods.
name = "Alice"
age = 30
formatted_string = f"My name is {name} and I am {age} years old."
print(formatted_string)
#String interpolation is the process of inserting variables or expressions into a string.
#F-strings provide a concise and readable way to achieve this.
#You can include expressions inside the curly braces as well
calculation = f"Five plus ten is {5 + 10}."
print(calculation)
#You can also use built-in string methods like upper(), lower(), strip(), replace(), and split()
sample = "  Hello, Python Programming!  "
print(sample.lower())        # '  hello, python programming!  '
print(sample.upper())        # '  HELLO, PYTHON PROGRAMMING!  '
print(sample.strip())       # 'Hello, Python Programming!'
print(sample.replace("Python", "Java"))  # '  Hello, Java Programming!
print(sample.split(","))    # ['  Hello', ' Python Programming!  ']
#These methods help in manipulating and analyzing strings effectively.  
#Let's explore some mathematical built-in functions.
