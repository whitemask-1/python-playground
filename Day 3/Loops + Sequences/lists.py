#The three basic sequence types in Python are lists, tuples, and ranges.

#Lists are mutable sequences, meaning their elements can be changed after creation. and can be comprised of
#strings, integers, floats, or even other lists.
#Lists are defined using square brackets [] and elements are separated by commas.

cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"]
print("Cities List:", cities)
print(type(cities))  # Outputs: <class 'list'>)

#You can access list elements using indexing (starting from 0) and slicing.
first_city = cities[0]  # 'New York'
last_city = cities[-1]  # 'Phoenix'

#Another way to create lists is by using the list() constructor.
#The list() constructor is used to convert an iterable into a list.
numbers = list(range(1, 6))  # Creates a list of numbers from 1 to 5
print("Numbers List:", numbers)
print(type(numbers))  # Outputs: <class 'list'>

#An iterable is any Python object capable of returning its members one at a time, allowing it to be looped over in a for-loop.
#Common examples of iterables include lists, tuples, strings, and ranges.
#To get total number of elements in a list, you can use the len() function.
print("Number of cities:", len(cities))  # Outputs: 5

#Lists support various methods for adding, removing, and modifying elements.
cities.append("San Francisco")  # Adds an element to the end of the list
print("After append:", cities)
cities.remove("Chicago")  # Removes the specified element from the list
print("After remove:", cities)
cities.sort()  # Sorts the list in ascending order
print("After sort:", cities)
cities.reverse()  # Reverses the order of the list
print("After reverse:", cities)
cities.insert(2, "Miami")  # Inserts 'Miami' at index 2
print("After insert:", cities)
cities[3] = "Seattle"  # Modifies the element at index 3
print("After modification:", cities)
del cities[1]  # Deletes the element at index 1
print("After deletion:", cities)
cities.extend(["Boston", "Denver"])  # Extends the list by adding elements from another list
print("After extend:", cities)
cities.pop()  # Removes and returns the last element of the list
print("After pop:", cities)
#You can specify an index in pop() to remove an element at a specific position.
removed_city = cities.pop(2)  # Removes and returns the element at index 2
print("Removed city:", removed_city)
print("After pop with index:", cities)
#To empty a list, you can use the clear() method.
#cities.clear()
#print("After clear:", cities)
#Also the sorted() function can be used to return a new sorted list from the elements of any iterable.
unsorted_numbers = [5, 2, 9, 1, 5, 6]
sorted_numbers = sorted(unsorted_numbers)  # Returns a new sorted list
print("Unsorted Numbers:", unsorted_numbers)
print("Sorted Numbers:", sorted_numbers)
#.index() method returns the index of the first occurrence of a specified value.
index_of_houston = cities.index("Houston")
print("Index of Houston:", index_of_houston)

# .find() method returns the lowest index of the substring if found in the string. If not found, it returns -1.



#To check if an element exists in a list, you can use the 'in' keyword.
if "Houston" in cities:
    print("Houston is in the list of cities.")
#Lists can also be nested, meaning you can have lists within lists.
nested_list = [[1, 2, 3], ["a", "b", "c"], [True, False]]
print("Nested List:", nested_list)
print("First element of nested list:", nested_list[0])  # [1, 2, 3]
print("Second element of first list in nested list:", nested_list[0][1])  # 2

#Then to access elements in a nested list, you can use multiple indexing.
#For example, nested_list[0][1] accesses the second element of the first list

#Unpacking lists is also possible in Python.
fruits = ["apple", "banana", "cherry"]
a, b, c = fruits  # Unpacks the list into individual variables
print("Unpacked fruits:", a, b, c)
#If you need to unpack only some elements, you can use the * operator.
numbers = [1, 2, 3, 4, 5]
first, *middle, last = numbers
print("First:", first)
print("Middle:", middle)
print("Last:", last)
#If there are more elements than variables, the * operator collects the remaining elements into a list.

#You can also access portions of a list using slicing.
sublist = cities[1:4]  # Gets elements from index 1 to
print("Sublist of cities:", sublist) # Outputs elements at index 1, 2, and 3




