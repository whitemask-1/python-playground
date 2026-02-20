# A linked list is a linear data structure in which each node is connected to the next node in the sequence.
# Each node contains two parts: data and a reference (or pointer) to the next node in the list.
# Unlike arrays, linked lists do not require contiguous memory allocation, allowing for dynamic memory usage and efficient insertions and deletions.

# Linked lists are commonly used for implementing other data structures such as stacks, queues, deques, and graphs.

# Singly Linked Lists:

# A singly linked list is a type of linked list where each node points to the next node in the sequence, and the last node points to None (indicating the end of the list).
# You start with a "head" node that serves as the entry point to the list.
# And you can traverse the list by following the next pointers from one node to the next until you reach the "tail".

# Time complexity for singly linked list operations:

# Insertion at the beginning: O(1) - Constant time complexity, as it involves updating the head pointer.
# Insertion at the end: O(n) - Linear time complexity, as it requires traversing the entire list to find the last node.
# Deletion at the beginning: O(1) - Constant time complexity, as it involves updating the head pointer.
# Deletion at the end: O(n) - Linear time complexity, as it requires traversing the entire list to find the second-to-last node.
# Search: O(n) - Linear time complexity, as it may require checking each node in the list.
# Insertion and deletion at a specific position: O(n) - Linear time complexity, as it may require traversing the list to reach the desired position.

#When to use:
# Singly linked lists are useful in scenarios where frequent insertions and deletions are required, especially at the beginning of the list.
# They are also beneficial when the size of the data is unknown or changes frequently, as they can dynamically grow and shrink in size without the need for resizing.
# However, singly linked lists do not provide efficient access to elements by index, as traversal is required to reach a specific position.

#Doubly Linked Lists:

# A doubly linked list is a type of linked list where each node contains three parts: data, a reference to the next node, and a reference to the previous node.
# This allows for traversal in both directions (forward and backward) through the list.
# The first node is called the "head", and the last node is called the "tail".
# In this type of linked list, its common to keep a reference to the tail node in the list structure itself to make operations at the end more efficient.
# They are more flexible than singly linked lists but require more memory due to the additional pointer.

# Time complexity for doubly linked list operations:

# Insertion at the beginning: O(1) - Constant time complexity, as it involves updating the head pointer and the previous pointer of the old head.
# Insertion at the end: O(1) - Constant time complexity, as it involves updating the tail pointer and the next pointer of the old tail.
# Deletion at the beginning: O(1) - Constant time complexity, as it involves updating the head pointer and the previous pointer of the new head.
# Deletion at the end: O(1) - Constant time complexity, as it involves updating the tail pointer and the next pointer of the new tail.
# Search: O(n) - Linear time complexity, as it may require checking each node in the list.
# Insertion and deletion at a specific position: O(n) - Linear time complexity, as it may require traversing the list to reach the desired position.

#When to use:
# Doubly linked lists are useful in scenarios where frequent insertions and deletions are required at both ends of the list.
# They are also beneficial when bidirectional traversal is needed, such as in navigation systems or undo/redo functionality.
# However, doubly linked lists require more memory due
