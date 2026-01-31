# Arrays are a fundamental data structure in programming that can be categorized into two types: static arrays and dynamic arrays.
# The difference between these two types lies in their size and memory allocation.

# Static Arrays:

# Static arrays have a fixed size that is determined at the time of their creation.
# Once a static array is created, its size cannot be changed.
# They are typically allocated on the stack memory, which allows for faster access times.
# However, this also means that if the array size is underestimated, it can lead to wasted memory, and if it is overestimated, it can lead to insufficient space for data storage.
# Accesing values of a static array takes O(1) time complexity.

#When to use:
# Static arrays are suitable for scenarios where the number of elements is known in advance and does not change frequently.
# They are often used in embedded systems or performance-critical applications where memory usage needs to be tightly controlled.
# Also helpful if values will be accessed frequently, as they provide fast access times.

# However static arrays cannot grow or shrink so if the number of elements stored can vary, dynamic arrays are a better choice.
# Trying to increase the size of a static array would require creating a new array and copying the existing elements over, which can be inefficient.

# Dynamic Arrays:

# Flexible in size and can grow or shrink as needed during runtime.
# Work through an automatic resizing mechanism that copies the elements into a new array when then original array is full
# Accessing elements of a dynamic array also takes O(1) time complexity on average, but resizing operations can take O(n) time in the worst case when the array needs to be expanded.
# Inserting and element in the middle of the array takes O(n) time complexity as well since elements need to be shifted.
# Insterting at the end of the array takes O(1) time complexity on average but if the array is full and needs to be resized it takes O(n) time complexity.

#When to use:
# Dynamic arrays are ideal for scenarios where the number of elements is not known in advance or can change frequently.
# They are commonly used in applications where data is continuously added or removed, such as in lists or collections that grow over time.
# They provide the flexibility to accommodate varying data sizes without the need for manual memory management.
# However, dynamic arrays may have higher overhead due to the resizing process and memory allocation, which can impact performance in scenarios with frequent insertions and deletions.

# Python's built-in list type is an example of a dynamic array, providing the ability to easily add, remove, and access elements while managing memory automatically.
numbers = [1, 2, 3, 4, 5]  # This is a dynamic array (list) in Python
numbers.append(6)          # Adding an element to the dynamic array
print(numbers)            # Output: [1, 2, 3, 4, 5, 6]