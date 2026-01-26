#A Tuple is a python data type that is an ordered, immutable collection of elements.
#Tuples are similar to lists, but unlike lists, tuples cannot be modified after their creation
#Tuples are defined using parentheses () and elements are separated by commas.
#Creating a tuple
my_tuple = (1, 2, 3, "Hello", 4.5)
print("My Tuple:", my_tuple)
print(type(my_tuple))  # Outputs: <class 'tuple'>

#Accessing tuple elements using indexing (starting from 0) and slicing
first_element = my_tuple[0]  # 1
last_element = my_tuple[-1]  # 4.5
print("First Element:", first_element)
print("Last Element:", last_element)

#You can also use a tuple() constructor to create a tuple from an iterable
list_example = [4, 5, 6, "World"]
another_tuple = tuple(list_example)

#To check if an item is in a tuple, you can use the 'in' keyword
if "World" in another_tuple:
    print("World is in the tuple.")

#Tuples support various methods, although they are limited due to their immutability    
count_of_5 = another_tuple.count(5)  # Counts occurrences of 5
index_of_6 = another_tuple.index(6)    # Finds index of first occurrence of 6
print("Count of 5 in another_tuple:", count_of_5)
print("Index of 6 in another_tuple:", index_of_6)

#What are some common methods for tuples?
sample_tuple = (10, 20, 30, 20, 40, 20)
print(sample_tuple.count(20))  # 3
print(sample_tuple.index(30))  # 2  # index() returns the index of the first occurrence of the specified value

#Tuples are often used to group related data together, especially when the data should not be modified.
#For example, you might use a tuple to represent a point in 2D space:
point = (3, 4)  # Represents the point (x=3, y=4)
print("Point in 2D space:", point)
#Tuples can also be used as keys in dictionaries due to their immutability.
coordinates_dict = {(1, 2): "Point A", (3, 4): "Point B"}

#Sorted tuples can be created by using the sorted() function, which returns a new sorted list from the elements of any iterable.
unsorted_tuple = (5, 2, 9, 1)
sorted_tuple = tuple(sorted(unsorted_tuple))  # Converts the sorted list back to a tuple
print("Unsorted Tuple:", unsorted_tuple)
print("Sorted Tuple:", sorted_tuple)

#If you need to customize the sorting order, you can use the optional reverse and key parameters of the sorted() function.
custom_sorted_tuple = tuple(sorted(unsorted_tuple, reverse=True))  # Sorts in descending order
print("Custom Sorted Tuple (Descending):", custom_sorted_tuple)

custom_sorted_by_mod_tuple = tuple(sorted(unsorted_tuple, key=lambda x: x % 3))  # Sorts based on modulus 3
print("Custom Sorted Tuple (by modulus 3):", custom_sorted_by_mod_tuple)

# Tuples can be unpacked into individual variables.
coordinates = (10, 20)
x, y = coordinates  # Unpacking the tuple
print("X Coordinate:", x)
print("Y Coordinate:", y)

#If there are more elements than variables, you can use the * operator to collect the remaining elements into a list.
data = (1, 2, 3, 4, 5)
first, *middle, last = data
print("First:", first)
print("Middle:", middle)
print("Last:", last)

#Tuples are useful for ensuring data integrity, as their immutability prevents accidental modifications.
#They are commonly used in functions to return multiple values, as dictionary keys, and in situations where a fixed collection of items is needed.
