#What are lambda functions?
#Lambda functions are small anonymous functions defined using the lambda keyword. They can take any number of arguments but can only have a single expression. The expression is evaluated and returned when the function is called.
#Basic Syntax:
#lambda arguments: expression
#Example 1: A simple lambda function that adds 10 to the input number
add_ten = lambda x: x + 10
print("Add 10 to 5:", add_ten(5))  # Output: 15

#To help with understanding we can map the pieces of a normal function to a lambda function
#Normal function:
def add_ten_normal(x):
    return x + 10
#Lambda function:
add_ten_lambda = lambda x: x + 10
print("Add 10 to 5 using normal function:", add_ten_normal(5))  # Output: 15
print("Add 10 to 5 using lambda function:", add_ten_lambda(5))  # Output: 15

#As you can see both functions do the same thing, but the lambda function is more concise.
#The parameter 'x' is the argument, and 'x + 10' is the expression that gets evaluated and returned.

#Example 2: A lambda function that multiplies two numbers
multiply = lambda a, b: a * b
print("Multiply 3 and 4:", multiply(3, 4))  # Output: 12

#Generally though lambda functions should not be used for variables since they are less readable than normal functions.
#It would also defeat the purpose of using an anonymous function.
#The real power of lambda functions comes from their ability to be defined inline.

#They are most useful when used as arguments to higher-order functions like map(), filter(), and reduce().
#Example 3: Using a lambda function with map() to square each number in a list
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x**2, numbers))
print("Squared numbers using map and lambda:", squared_numbers)  # Output: [1, 4, 9, 16, 25]

#Example 4: Using a lambda function with filter() to get even numbers from a list
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers using filter and lambda:", even_numbers)  # Output: [2, 4]

#Example 5: Using a lambda function with reduce() to calculate the product of all numbers in a list
from functools import reduce
product = reduce(lambda x, y: x * y, numbers)
print("Product of all numbers using reduce and lambda:", product)  # Output: 120

#reduce() is not a built-in function so it needs to be imported from the functools module.
#It applies the lambda function cumulatively to the items of the iterable, reducing it to a single value.

