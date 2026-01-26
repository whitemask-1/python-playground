#What are list comprehensions?

#List comprehensions are a concise way to create lists in Python. They provide a syntactically more compact and often more readable way to generate lists compared to traditional for loops.
#List comprehensions consist of brackets containing an expression followed by a for clause, and can also include optional if clauses to filter items.

#Basic Syntax:
#new_list = [expression for item in iterable if condition]

#Example 1: Creating a list of squares of numbers from 0 to 9

squares = [x**2 for x in range(10)]
print("Squares of numbers from 0 to 9:", squares)

#Example 2: Creating a list of even numbers from 0 to 19

evens = [x for x in range(20) if x % 2 == 0]
print("Even numbers from 0 to 19:", evens)

#Example 3: Creating a list of uppercase letters from a given string

input_string = "hello world"
uppercase_letters = [char.upper() for char in input_string if char.isalpha()]
print("Uppercase letters from the string 'hello world':", uppercase_letters)

#Example 4: Creating a list of tuples (number, square) for numbers from 0 to 4

number_square_tuples = [(x, x**2) for x in range(5)]
print("Tuples of (number, square) for numbers from 0 to 4:", number_square_tuples)

#Another way to create a list starting from an existing iterable is the filter() function
#Example 5: Using filter() to create a new list of just words with more than 3 letters
words = ["apple", "is", "banana", "to", "cherry", "at"]
long_words = list(filter(lambda word: len(word) > 3, words)) #Really cool use of lambda functions here
print("Words with more than 3 letters:", long_words)

#Another function to be aware of is the map() function which applies a function to all items in an input list (or any iterable)
#Example 6: Using map() to create a new list of squares of numbers from 0 to 9
numbers = range(10)
squared_numbers = list(map(lambda x: x**2, numbers)) #A good way to remember is that you can "map" a function to all items in an iterable
print("Squares of numbers from 0 to 9 using map():", squared_numbers)

#What is the difference between list comprehensions, filter(), and map()?
#List comprehensions provide a more readable and concise way to create lists, especially when filtering and transforming data in a single step.
#filter() is specifically used for filtering items from an iterable based on a condition, while map() is used for applying a function to each item in an iterable.

