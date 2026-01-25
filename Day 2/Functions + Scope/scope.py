#Scope determines the point at which a variable is accessible in the code.
#To correctly determine the scope, Python follows the LEGB rule:
#L: Local — Names assigned within a function (def or lambda), and not declared global
#E: Enclosing — Names in the local scope of any and all enclosing functions (def
#G: Global (module) — Names assigned at the top-level of a module file, or declared global in a def within the file
#B: Built-in (Python) — Names preassigned in the built-in names module
#Let's explore each of these scopes with examples.
#Global Scope
x = "global x"  # Global variable
def outer_function():
    #Enclosing Scope
    y = "enclosing y"  # Enclosing variable
    def inner_function():
        #Local Scope
        z = "local z"  # Local variable
        print(z)  # Accessing local variable
        print(y)  # Accessing enclosing variable
        print(x)  # Accessing global variable
    inner_function()
outer_function()
print(x)  # Accessing global variable
#The following lines would raise an error because y and z are not in the global scope
# print(y)  # Uncommenting this line will raise a NameError
# print(z)  # Uncommenting this line will raise a NameError
#Built-in Scope
print(len("Hello"))  # Using built-in function len()
#If you try to access a variable that is not found in the local, enclosing, or global scopes, Python will look for it in the built-in scope.
#Understanding scope is essential for managing variable lifetimes and avoiding naming conflicts in your code.
#It helps you write cleaner and more maintainable programs by controlling where variables can be accessed and modified.
#Let's look at an example of using functions to encapsulate code logic.
def square(num):
    """This function returns the square of a number."""
    return num ** 2
result = square(5)
print("Square of 5 is:", result)  # Outputs: Square of 5 is: 25
#In this example, the variable num is in the local scope of the function square.
#The variable result is in the global scope.
#You can also have nested functions, where an inner function has access to the variables of its enclosing function.
def outer():
    outer_var = "I am from outer function"
    def inner():
        inner_var = "I am from inner function"
        print(inner_var)  # Accessing inner variable
        print(outer_var)  # Accessing outer variable
    inner()
outer()
#In this example, the inner function can access both its own local variable inner_var and the enclosing variable outer_var.
#However, the outer function cannot access the inner function's local variable.
#Understanding how scope works in Python is crucial for writing effective and bug-free code.
#What about global and nonlocal keywords?
def counter():
    count = 0  # Local variable
    def increment():
        nonlocal count  # Refers to the nearest enclosing scope variable
        count += 1
        return count
    return increment
my_counter = counter()
print(my_counter())  # Outputs: 1
print(my_counter())  # Outputs: 2
#We need to use a nonlocal keyword to modify the count variable from the enclosing scope.
#If we had used global instead, it would refer to a variable in the global scope, which is not what we want in this case.
#Understanding the use of global and nonlocal keywords is important for managing variable scopes effectively in nested functions.

#Global keyword example
total = 0  # Global variable
def add_to_total(amount):
    global total  # Refers to the global variable
    total += amount
add_to_total(5)
print("Total after adding 5:", total)  # Outputs: Total after adding 5: 5
add_to_total(10)
print("Total after adding 10:", total)  # Outputs: Total after adding 10
#In this example, we use the global keyword to modify the global variable total from within the function add_to_total.
#Without the global keyword, Python would treat total as a local variable within the function, leading to an UnboundLocalError.

#An easy way to remember global and nonlocal is:
#Use global when you want to refer to a variable defined at the top-level of the module
#Use nonlocal when you want to refer to a variable defined in the nearest enclosing function scope