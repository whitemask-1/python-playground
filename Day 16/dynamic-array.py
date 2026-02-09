import ctypes

class DynamicArray:
    
    # Here, we implement manual resizing/removal to understand how arrays work under the hood.
    def __init__(self, capacity=int):
        self._n = 0 #number of elements
        self._capacity = capacity if capacity > 0 else 1
        self._A = self._make_array(self._capacity)

    def __len__(self):
        return self._n
    
    def __getItem__(self, i):
        if not 0 <= i <= self._n:
            raise IndexError(f"{i} not found within array index")
        return self._A[i]
    
    def append(self, value):
        if self._n == self._capacity:
            self._resize(self._capacity * 2) # Double up capacity to decrease how often we have to resize
        self._A[self._n] = value # _n is always 1 ahead of index as it holds the number of elements making it perfect for adding to the end
        self._n += 1 # Update _n value so that this function keeps working and the value is still valid
    
    def insert(self, value, i):
        left, right = self._A[:i], self._A[i:]


    def _make_array(self, cap): # Using a regular Python list would already provide dynamic resizing.
        return cap * ctypes.py_object()

    def _resize(self, new_cap):
        B = self._make_array(new_cap) 
        for i in range(self._n):
            B[i] = self._A[i]
        self._A = B
        self._capacity = new_cap

    # Essential functions for a dynamic array:
    # - __len__: Return the number of elements.
    # - __getitem__: Access element at a given index.
    # - append: Add an element to the end, resizing if needed.
    # - insert: Add an element at a specific index.
    # - remove: Remove an element by value.
    # - pop: Remove and return element at a given index.
    # - resize: Internal method to grow/shrink the array.
    # - __str__ or __repr__: String representation for debugging.

    # You can implement these step by step!

