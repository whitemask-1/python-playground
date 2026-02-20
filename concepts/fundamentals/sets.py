# Sets are one of the built-in data types in Python that store unordered collections of unique elements.
# Sets are mutable, meaning you can add or remove elements after creation.
# Sets are defined using curly braces {} or the set() constructor.

#Basic Syntax:
#my_set = {element1, element2, ...}
#Example 1: Creating a simple set
fruits = {"apple", "banana", "cherry", "date"}
print("Fruits Set:", fruits)
print(type(fruits))  # Outputs: <class 'set'>

# One quirk of sets is that if you need to define an empty set, you must use the set() constructor.
# This is because using {} creates an empty dictionary, not a set.
empty_set = set()
print("Empty Set:", empty_set)
print(type(empty_set))  # Outputs: <class 'set'>

#You can add elements to a set using the add() method.
fruits.add("elderberry")
print("After adding elderberry:", fruits)

#You can remove elements from a set using the remove() or discard() methods.
fruits.remove("banana")  # Raises KeyError if the element is not found
print("After removing banana:", fruits)
fruits.discard("fig")  # Does not raise an error if the element is not found
print("After discarding fig (not present):", fruits)

#You can use .clear() method to remove all elements from a set.
#fruits.clear()
#print("After clear:", fruits)

# Python sets also have .issubset() and .issuperset() methods to check subset and superset relationships.
A = {1, 2, 3}
B = {1, 2, 3, 4, 5}
print("Is A a subset of B?", A.issubset(B))  # True
print("Is B a superset of A?", B.issuperset(A))  # True

#The isdisjoint() method checks if two sets have no elements in common.
C = {6, 7, 8}
print("Are A and C disjoint?", A.isdisjoint(C))  # True

# The union operator '|' combines two sets, returning a new set with all unique elements from both sets.
union_set = A | C
print("Union of A and C:", union_set)  # {1, 2, 3, 6, 7, 8}

# The intersection operator '&' returns a new set with elements common to both sets.
D = {2, 3, 4}
intersection_set = A & D
print("Intersection of A and D:", intersection_set)  # {2, 3}

# The difference operator '-' returns a new set with elements in the first set that are not in the second set.
difference_set = B - A
print("Difference of B and A (B - A):", difference_set)  # {4, 5}

# The symmetric difference operator '^' returns a new set with elements in either set but not in both.
symmetric_difference_set = A ^ D
print("Symmetric Difference of A and D:", symmetric_difference_set)  # {1, 4}

#Each of these operators also has its corresponding in-place version (|=, &=, -=, ^=) that modifies the original set instead of creating a new one.
E = {1, 2, 3}

E |= {4, 5}  # In-place union
print("After in-place union (E |= {4, 5}):", E)

E &= {2, 3, 4}  # In-place intersection
print("After in-place intersection (E &= {2, 3, 4}):", E)

E -= {3}  # In-place difference
print("After in-place difference (E -= {3}):", E)

E ^= {1, 4}  # In-place symmetric difference
print("After in-place symmetric difference (E ^= {1, 4}):", E)

#You can check whether an element exists in a set using the 'in' keyword.
if 2 in A:
    print("2 is in set A.")

#Sets are particularly useful for membership testing and eliminating duplicate entries from a collection.
#They are also commonly used in mathematical operations involving sets, such as unions, intersections, and differences.
#Remember that since sets are unordered, the elements may appear in a different order each time you print the set.
#This is because sets do not maintain any specific order for their elements.

#Also, since sets only store unique elements, any duplicate values added to a set will be ignored.
#For example:
duplicate_set = {1, 2, 2, 3, 4, 4, 4}
print("Set with duplicates added:", duplicate_set)  # Output: {1, 2, 3, 4}
#As you can see, the duplicates were removed automatically.

#The data type of elements in a set must be immutable (hashable).
#This means you can have elements like strings, numbers, or tuples (if the tuple contains only immutable elements).
#However, you cannot have lists or dictionaries as elements of a set since they are mutable.

#For example, the following line would raise a TypeError:
# invalid_set = {1, 2, [3, 4]}  # This will raise a TypeError