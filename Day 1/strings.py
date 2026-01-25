#Using single quotes to define a string that contains double quotes
quote = 'She said, "Hello, World!"'
print(quote) #But can it be used vice versa?

#Using double quotes to define a string that contains single quotes
contraction = "It's a beautiful day!"
print(contraction)

#You can also use escape characters to include quotes within strings
escaped_single = 'It\'s a sunny day!'
print(escaped_single)

#What about Multi-line strings?
multi_line = '''This is a multi-line string.
It can span multiple lines.
Useful for long texts.'''
print(multi_line) #I think by this point you understand quotation marks are interchangeable in Python

#We can also check for words in strings with the 'in' keyword
sentence = "The quick brown fox jumps over the lazy dog."
word1 = "fox"
word2 = "cat"
print(word1 in sentence)  # True
print(word2 in sentence)  # False
print("quick" in sentence)  # True

#Theres also the len() function to check the length of a string
sample_string = "Hello, Python!"
length = len(sample_string)
print("Length of the string:", length)

#Each character in a string has an index, starting from 0
first_char = sample_string[0]  # 'H'
fifth_char = sample_string[4]  # 'o'
last_char = sample_string[-1]   # '!'
print("First character:", first_char)
print("Fifth character:", fifth_char)
print("Last character:", last_char) #As you see we can navigate into negative numbers aswell in order to access characters from the end of the string

#Can we also set a variable to be a range of indexes?
substring = sample_string[7:13]  # 'Python'
print("Substring from index 7 to 12:", substring) #String slicing discovered!

#Strings are immutable, meaning we cannot change them directly
#For example, the following line would raise an error:      
# sample_string[0] = 'h'  # This will raise a TypeError
#To counter this we can use string concatenation to create a new string
new_string = 'h' + sample_string[1:]  # 'hello, Python!'
print("New string after modification:", new_string)#Not you cannot use anything other than strings to concatenate with strings, it will raise an error
#You must first convert other data types to strings using the str() function
number = 42
combined = "The answer is: " + str(number)
print(combined)

#You can also use += operator to append to strings
greeting = "Hello"
greeting += ", World!"
print(greeting)

#These are just a few of the many string methods available in Python. Strings are versatile and powerful for text manipulation!
#You can also use formatted strings (f-strings) for easier string interpolation (Python 3.6+)
name = "Alice"
age = 30
formatted_string = f"My name is {name} and I am {age} years old."
print(formatted_string)

#String interpolation is the process of inserting variables or expressions into a string.
#F-strings provide a concise and readable way to achieve this.
#You can include expressions inside the curly braces as well
calculation = f"Five plus ten is {5 + 10}."
print(calculation)

#What about string slicing, How does that work?
slice_example = "Hello, World!"
print(slice_example[0:5])  # 'Hello'
print(slice_example[7:12]) # 'World'
print(slice_example[:5])   # 'Hello'
print(slice_example[7:])   # 'World!'
print(slice_example[-6:-1]) # 'World'
#String slicing allows you to extract a portion of a string by specifying start and end indices.
#You can also specify a step value
step_example = "abcdefghij"
print(step_example[::2])  # 'acegi' (every second character)
print(step_example[1::2]) # 'bdfhj' (every second character starting # from index 1)
#step parameters in slicing allow you to skip characters in the specified range. in the syntax of [start:end:step], the step determines the interval between characters to include in the slice.
#Note that the last index is exclusive, meaning it is not included in the result.

#What are some common string methods? and what are string methods anyway?
#String methods are built-in functions that perform specific operations on strings.
sample = "  Hello, Python Programming!  "
print(sample.lower())        # '  hello, python programming!  '
print(sample.upper())        # '  HELLO, PYTHON PROGRAMMING!  '
print(sample.strip())       # 'Hello, Python Programming!'
print(sample.replace("Python", "Java"))  # '  Hello, Java Programming!
print(sample.split(","))    # ['  Hello', ' Python Programming!  ']
print(sample.find("Python")) # 8
print(sample.startswith("  Hello")) # True
print(sample.endswith("!  "))  # True
print(sample.count("o"))    # 4
print(sample.capitalize())  # '  hello, python programming!  '
print(sample.strip().capitalize())  # 'Hello, python programming!'
#These methods help in manipulating and analyzing strings effectively.
# As for definitions for each method:
# lower(): Converts all characters in the string to lowercase.
# upper(): Converts all characters in the string to uppercase.
# strip(): Removes leading and trailing whitespace from the string.
# replace(old, new): Replaces occurrences of a specified substring (old) with another substring
# split(separator): Splits the string into a list of substrings based on the specified separator.
# find(substring): Returns the lowest index of the substring if found in the string; otherwise
# startswith(prefix): Checks if the string starts with the specified prefix; returns True or False.
# endswith(suffix): Checks if the string ends with the specified suffix; returns True or
# count(substring): Counts the occurrences of a specified substring in the string.
# capitalize(): Capitalizes the first character of the string and lowercases the rest.
#These are just a few examples; Python provides many more string methods for various operations.
#To see them all you can refer to the official Python documentation on string methods:
#https://docs.python.org/3/library/stdtypes.html#string-methods

