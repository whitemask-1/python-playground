# Stacks and queues are linear data structures that follow specific orderings for adding and removing elements.

#Stacks:
# A stack is a Last In First Out (LIFO) data structure, meaning the last element added to the stack is the first one to be removed.
# Stacks have two ends, known as the "top" and "bottom". Elements are added and removed from the top of the stack.

# Elements are added and removed from the top of the stack using two primary operations:
# 1. Push: Adds an element to the top of the stack.
# 2. Pop: Removes and returns the element from the top of the stack.

# Time complexity for stack operations:
# Push operation: O(1) - Constant time complexity, as it involves adding an element to the top of the stack.
# Pop operation: O(1) - Constant time complexity, as it involves removing an element from the top of the stack.
# Peek operation: O(1) - Constant time complexity, as it involves accessing the top element without removing it.

#When to use:
# Stacks are useful in scenarios where you need to reverse the order of elements, such as in function call management (call stack), expression evaluation, and backtracking algorithms.
# Example of a stack using Python list
stack = []
stack.append(1)  # Push operation
stack.append(2)  # Push operation
top_element = stack.pop()  # Pop operation, removes 2
print(top_element)  # Output: 2

#Technically its only a stack because of the way we use it. Python lists can be used as stacks but they are not limited to stack operations only.

#Queues:
# A queue is a First In First Out (FIFO) data structure, meaning the first element added to the queue is the first one to be removed.
# Queues have two ends, known as the "front" and "back". Elements are added at the back and removed from the front

# Elements are added and removed using two primary operations:
# 1. Enqueue: Adds an element to the back of the queue.
# 2. Dequeue: Removes and returns the element from the front of the queue.

# Time complexity for queue operations:
# Enqueue operation: O(1) - Constant time complexity, as it involves adding an element to the back of the queue.
# Dequeue operation: O(1) - Constant time complexity, as it involves removing an element from the front of the queue.
# Peek operation: O(1) - Constant time complexity, as it involves accessing the front element without removing it.

#When to use:
# Queues are useful in scenarios where you need to maintain the order of elements, such as in task scheduling, breadth-first search algorithms, and handling requests in web servers.
# Example of a queue using Python's collections.deque for efficient O(1) operations
from collections import deque
queue = deque()
queue.append(1)  # Enqueue operation
queue.append(2)  # Enqueue operation
front_element = queue.popleft()  # Dequeue operation, removes 1
print(front_element)  # Output: 1