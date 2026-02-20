# A priority queue is an abstract data type that operates similar to a regular queue or stack data structure,
# but with an added feature: each element in a priority queue has a priority associated with it
# Elements with higher priority are served before elements with lower priority.
# Priority queues are helpful for finding the shortest past, scheduling tasks, simulating traffic, compressing data, and managing networks

# They are commonly implemented using heaps, which are specialized tree-based data structures that satisfy the heap property.
# In a max-heap, for any given node, the value of the node is greater than or equal to the values of its children.
# In a min-heap, for any given node, the value of the node is less than or equal to the values of its children.

# This property allows for efficient retrieval of the highest (or lowest) priority element.
# It also ensures that the maximum (or minimum) element is always at the root of the heap, which makes it easy to access.

# Heaps are typically implemented as arrays to access parent and child nodes efficiently using index calculations.
# For a node at index i:
# - The left child is located at index 2i + 1
# - The right child is located at index 2i + 2
# - The parent node is located at index (i - 1) // 2

# Python has a built-in library called heapq that provides an efficient implementation of a min-heap.
import heapq
#It works by operating on a list, following specific steps that work with the elements as if the list was a heap, preserving the heap property.
my_heap = []  # Initialize an empty list to represent the heap
heapq.heappush(my_heap, 5)  # Add element 5 to the heap
heapq.heappush(my_heap, 2)  # Add element 2 to the heap
heapq.heappush(my_heap, 8)  # Add element 8 to the heap
smallest = heapq.heappop(my_heap)  # Remove and return the smallest element (2)
heapq.heappushpop(my_heap, 3)  # Push 3 and pop the smallest element (3)
# pushpop is more efficient than doing a separate push followed by a pop since it performs one operaton instead of two

# If you already have a list and what to transform it into a heap you could call heapify()
my_list = [7, 1, 4, 6, 3]
heapq.heapify(my_list)  # Transform the list into a heap in-place
# Now my_list is a valid min-heap

# To implement a max-heap using heapq, you can invert the values by multiplying them by -1 when adding and removing elements.
max_heap = []
heapq.heappush(max_heap, -5)  # Add element 5 (inverted to -5)
heapq.heappush(max_heap, -2)  # Add element 2 (inverted to -2)
heapq.heappush(max_heap, -8)  # Add element 8 (inverted to -8)
largest = -heapq.heappop(max_heap)  # Remove and return the largest element (8, inverted back to positive)

# To sort by priority instead of value, you can use tuples where the first element is the priority and the second element is the value.
priority_queue = []
heapq.heappush(priority_queue, (2, 'task 2'))  # Task with priority 2
heapq.heappush(priority_queue, (1, 'task 1'))  # Task with priority 1
heapq.heappush(priority_queue, (3, 'task 3'))  # Task with priority 3
highest_priority_task = heapq.heappop(priority_queue)  # Removes and returns the task with the highest priority (1, 'task 1')
# Lower numerical values indicate higher priority in this example

# The reason heaps are typically implemented as arrays is due to their efficient use of space and time.