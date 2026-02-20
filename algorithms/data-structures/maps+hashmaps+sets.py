# Abstract Data Types: Maps, Hashmaps, and Sets
# An absstract data type (ADT) is a conceptual representation of a data type, including what operations can be performed on the data and the properties of the data
# ADTs are like the blueprints to descript what operations can be performed on a data structure, without specifying how these operations are implemented.
# Maps, hashmaps, and sets are common ADTs used in programming to organize and manipulate data efficiently.

# Maps:
# A map is an abstract data type that represents a collection of key-value pairs, where each key is unique and maps to a specific value.
# Maps allow for efficient retrieval, insertion, and deletion of values based on their associated keys because of unique keys.

# Common operations on maps:
# 1. Insertion: Add a key-value pair to the map.
# 2. Deletion: Remove a key-value pair from the map using its key.
# 3. Lookup: Retrieve the value associated with a specific key. (Check if key exists)
# 4. Update: Modify the value associated with a specific key.

# Time complexity for map operations:
# Insertion: O(1) - Average case constant time complexity, as it involves adding a key-value pair to the map.
# Deletion: O(1) - Average case constant time complexity, as it involves removing a key-value pair from the map.
# Lookup: O(1) - Average case constant time complexity, as it involves accessing the value associated with a specific key.
# Update: O(1) - Average case constant time complexity, as it involves modifying the value associated with a specific key.

#When to use:
# Maps are useful in scenarios where you need to associate unique keys with specific values, such as in databases, caching systems, and configuration settings.
# They provide efficient access to data based on keys, making them ideal for applications that require fast lookups and updates.
# Example of a map using Python's built-in dictionary
my_map = {}
my_map["apple"] = 1      # Insertion
my_map["banana"] = 2     # Insertion
print(my_map["apple"])    # Lookup, Output: 1

# Hashmaps:
# A hashmap is a implementation of the map ADT that uses a technique called hashing to perform operations efficiently.
# Hashing works by generating a hash value (a fixed-size integer) for each element using a hash function.
# The hash value is generated based on the kay of the key-value pair, and it determines the index where the value will be stored in an underlying array.
# This allows for fast access to values based on their keys, as the hash value can be used to directly compute the index in the array.

# What happens when two keys produce the same hash value? This is called a collision.
# Common collision resolution techniques include:
# 1. Chaining: Each index in the array contains a linked list of key-value pairs that hash to the same index.
# 2. Open Addressing: When a collision occurs, the algorithm searches for the next available index in the array to store the key-value pair.

# Time complexity for hashmap operations:
# Insertion: O(1) - Average case constant time complexity, as it involves computing the hash value and adding the key-value pair to the hashmap.
# Deletion: O(1) - Average case constant time complexity, as it involves computing the hash value and removing the key-value pair from the hashmap.
# Lookup: O(1) - Average case constant time complexity, as it involves computing the hash value and accessing the value associated with a specific key.
# Update: O(1) - Average case constant time complexity, as it involves computing the hash value and modifying the
# The worst case time complexity for these operations can degrade to O(n) if there are many collisions, but with a good hash function and proper resizing, this is rare.

#When to use:
# Hashmaps are useful in scenarios where you need fast access to data based on unique keys, such as in caching systems, symbol tables in compilers, and associative arrays.
# They provide efficient access to data and can handle large datasets effectively.
# Example of a hashmap using Python's built-in dictionary
hashmap = {}
hashmap["name"] = "Alice"  # Insertion
hashmap["age"] = 30        # Insertion
print(hashmap["name"])     # Lookup, Output: Alice

# Whats the difference between maps and hashmaps?
# Maps are abstract data types that define the behavior of key-value pair collections, while hashmaps are a specific implementation of the map ADT that uses hashing for efficient operations.

# Sets:
# A set is an abstract data type that represents a collection of unique elements, meaning that no duplicate values are allowed.
# Sets are commonly used for membership testing, removing duplicates from a collection, and performing mathematical set operations such as union, intersection, and difference.
# Sets are not ordered, meaning that the elements do not have a specific order.
# Sets are also dynamic, meaning that they can grow and shrink in size as elements are added or removed.

# Common operations on sets:
# 1. Insertion: Add an element to the set.
# 2. Deletion: Remove an element from the set.
# 3. Membership Testing: Check if an element is present in the set.
# 4. Union: Combine two sets to create a new set containing all unique elements from both sets.
# 5. Intersection: Create a new set containing only the elements that are present in both sets.
# 6. Difference: Create a new set containing elements that are present in one set but not in the other.

# Time complexity for set operations:
# Insertion: O(1) - Average case constant time complexity, as it involves adding an element to the set.
# Deletion: O(1) - Average case constant time complexity, as it involves removing an element from the set.
# Membership Testing: O(1) - Average case constant time complexity, as it involves checking if an element is present in the set.
# Union: O(n) - Linear time complexity, as it involves combining elements from both sets.
# Intersection: O(n) - Linear time complexity, as it involves checking elements from both sets.
# Difference: O(n) - Linear time complexity, as it involves checking elements from both sets.

#When to use:
# Sets are useful in scenarios where you need to maintain a collection of unique elements, such as in database operations, data analysis, and graph algorithms.
# They provide efficient membership testing and support mathematical set operations.
# Example of a set using Python's built-in set type
my_set = set()
my_set.add(1)        # Insertion
my_set.add(2)        # Insertion
my_set.add(1)        # Insertion (duplicate, will not be added)
print(my_set)       # Output: {1, 2}

# Behind the scenes, Python's set is implemented using a hashmap without values, which is why set operations have average case O(1) time complexity.
# Note that sets are immutable, meaning that the elements themselves cannot be changed once added to the set.
# However, you can add or remove elements from the set itself.