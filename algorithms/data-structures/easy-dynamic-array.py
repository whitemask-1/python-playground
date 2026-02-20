# Essential functions for a dynamic array:
    # - __len__: Return the number of elements.
    # - __getitem__: Access element at a given index.
    # - append: Add an element to the end, resizing if needed.
    # - insert: Add an element at a specific index.
    # - remove: Remove an element by value.
    # - pop: Remove and return element at a given index.
    # - resize: Internal method to grow/shrink the array.
    # - __str__ or __repr__: String representation for debugging.

class DynamicArray:
    def __init__(self):
        self._A = []
    
    def insert(self, value):
        self._A.append(value)
    
    def remove(self, value):
        self._A.remove(value)
    
    def pop(self, value):
        self._A.pop(value)
    