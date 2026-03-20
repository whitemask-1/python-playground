Linked Lists
    - Linked lists are made up of nodes
    - Nodes have and **value** and a **pointer** to the next node
    - The last node points to None

Runtime complexity of O(n)

Doubly Linked Lists - nodes also have a pointer to the previous node
    - First node points back to None

##  Node Class:
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
- Every node initialized with a value and a pointer to the next
    - By default the node points to None

## Linked List Class

- Linked Lists have a head node which is the first node
    - All other nodes come after the head node

### append method

- to append to the end of the list
    - first check if there is already a head value of the linked list
        - if not assign the new value as a node to the head
    - else find the next node in the list without a next value
        - assign the new value as a node to the .next of the node

### prepend method

- to prepend to the beginning of the list
    - initialize the node with a value
    - set the pointer for the node to the head
    - set the head of the linked list to the new node

### insert method

- to insert a value at a declared index
    - if the index is 0 then we can use the prepend method to insert at the front
    - else we iterate through the linked list for i times in range(index-1)
        - if there is no value or we find a node with a .next of None
            - return a indexerror
        - upon finding the indexed node before the index value
            - set the new node to point at the same next node
            - point the index node at the new node


