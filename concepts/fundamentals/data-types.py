#showcase understanding of variables and data types in Python

#Integer -  whole number
my_integer = 10
print(my_integer)

#Float - decimal number
my_float = 10.5
print(my_float)

#String - sequence of characters
my_string = "Hello, Python!"
print(my_string)

#Boolean - True or False
my_boolean = True
print(my_boolean)

#Set - unordered, mutable collection of unique elements
my_set = {1, 2, 3, 4, 5}
print(my_set)

#List - ordered, mutable collection
my_list = [1, 2, 3, 4, 5]
print(my_list)

#Dictionary - key-value pairs
my_dict = {'name': 'Alice', 'age': 30}
print(my_dict)

#range - immutable sequence of numbers within a specified range
my_range = range(1, 10)
print(list(my_range)) #list function is used to display range values

#Tuple - ordered, immutable collection
my_tuple = (1, 2, 3, 4, 5)  
print(my_tuple)

#NoneType - represents the absence of a value
my_none = None
print(my_none)

#Complex Number - number with a real and imaginary part
my_complex = 2 + 3j #2D coordinate system/vectors
print(my_complex)

print (type(my_integer)) #type() function to check data type
print (type(my_float))
print (type(my_string))
print (type(my_boolean))
print (type(my_set))

print (isinstance(my_list, list)) #isinstance() function to check if variable is of a specific data type
print (isinstance(my_dict, dict)) #follows form isinstance(variable, type to check)#
print (isinstance(my_tuple, tuple))
print (isinstance(my_none, type(None)))
print (isinstance(my_complex, complex))