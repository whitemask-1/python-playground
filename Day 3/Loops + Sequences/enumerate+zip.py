# The enumerate() function adds a counter to an iterable and returns it as an enumerate object.
# This is particularly useful when you need both the index and the value while iterating over a sequence.
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(f"Index: {index}, Fruit: {fruit}")

# You can also specify a starting index for the counter.
for index, fruit in enumerate(fruits, start=1):
    print(f"Index: {index}, Fruit: {fruit}")