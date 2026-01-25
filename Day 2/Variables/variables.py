#variables store data values that can be used and manipulated throughout your code.
#variables refer to a memory location where data is stored.
#In Python, you don't need to declare the type of a variable explicitly; it is inferred from the value assigned to it.
#Variables cannot use reserved keywords in Python (like if, else, while, etc.) as names.
#Variable names should start with a letter (a-z, A-Z) or an underscore (_) followed by letters, digits (0-9), or underscores.
#Variable names are case-sensitive (e.g., myVar and myvar are different variables).
#Here are some examples of valid variable names:
my_variable = 10
user_name = "Alice"
is_active = True
pi_value = 3.14
_if = "valid variable name starting with underscore"

#Python developers commonly use snake_case for variable names, where words are separated by underscores.
#You can assign values to multiple variables in a single line:
x, y, z = 1, 2.5, "Hello"
print("x:", x)
print("y:", y)
print("z:", z)

#You can also assign the same value to multiple variables:
a = b = c = 100
print("a:", a)
print("b:", b)
print("c:", c)

#Getting user input and storing it in a variable:
age = input("Enter your age: ")
print("You entered:", age)

#Remember that input() function returns a string, so if you need a different data type, you must convert it using int(), float(), etc.
age_int = int(age)  # Convert the input string to an integer
print("Your age next year will be:", age_int + 1)
print("age_int data type:", type(age_int))  # This will show that age_int is of type 'int'

#Casting between data types:
num_str = "123"
num_int = int(num_str)      # Converts string to integer
num_float = float(num_str)  # Converts string to float
print("String:", num_str)
print("Converted to Integer:", num_int)
print("Converted to Float:", num_float)

#You can also use the built-in functions to check the type of a variable using type()
print("Type of my_variable:", type(my_variable))  # Output: <class 'int
print("Type of user_name:", type(user_name))      # Output: <class 'str'>
print("Type of is_active:", type(is_active))      # Output: <class 'bool
print("Type of pi_value:", type(pi_value))        # Output: <class 'float'>

#Variables are fundamental in programming as they allow you to store, retrieve, and manipulate data efficiently.
#They are essential for creating dynamic and interactive programs.
#Remember to choose meaningful variable names that reflect the purpose of the data they hold, as this improves code readability and maintainability.
#Let's explore variable reassignment
my_variable += 20
print("Initial my_variable:", my_variable)  # Output: 30
my_variable = 20  # Reassigning a new value to the same variable
print("Reassigned my_variable:", my_variable)  # Output: 20

#You can also change the data type of a variable by assigning a value of a different type
my_variable = "Now I'm a string"
print("my_variable after changing type:", my_variable)  # Output: Now I'm a string
print("Type of my_variable after changing type:", type(my_variable))  # Output: <class 'str'>

