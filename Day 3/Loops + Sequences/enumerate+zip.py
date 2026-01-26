# The enumerate() function adds a counter to an iterable and returns it as an enumerate object.
# This is particularly useful when you need both the index and the value while iterating over a sequence.
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(f"Index: {index}, Fruit: {fruit}")

# You can also specify a starting index for the counter.
for index, fruit in enumerate(fruits, start=1):
    print(f"Index: {index}, Fruit: {fruit}")

#What if we want to iterate over multiple iterables in parallel?
# The zip() function combines multiple iterables (like lists or tuples) into a single iterable of tuples.
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
for name, age in zip(names, ages):
    print(f"Name: {name}, Age: {age}")

# If the iterables are of different lengths, zip() stops creating tuples when the shortest iterable is exhausted.

#You can also unzip a list of tuples using the zip() function with the unpacking operator
zipped = [('Alice', 25), ('Bob', 30), ('Charlie', 35)]
names, ages = zip(*zipped)
print("Names:", names)
print("Ages:", ages)

#Both enumerate() and zip() are powerful tools for working with sequences in Python, making it easier to manage indices and parallel iteration.