# Trees are a specific type of graph that has unique properties and characteristics.
# A tree is an acyclic connected graph, meaning it has no cycles and there is a path between any two nodes.
# Trees are often used to represent hierarchical structures, such as file systems, organizational charts, and decision trees.
# The root node is the very top of a tree. Its the only node in the tree without a parent node and is usually where you start traversing the tree.
# Each node in a tree can have zero or more child nodes, which are the nodes directly connected to it below.
# Nodes that have the same parent are called siblings.
# Nodes with no children are called leaf nodes or terminal nodes.

# There are a few important properties of trees to be aware of:
#   The height of a tree is the length of the longest path from the root node to a leaf node.
#   The depth of a node is the length of the path from the root node to that specific node.
#   The degree of a node is the number of children it has.


# The two most common types of trees are binary trees and binary search trees (BSTs):

# In a binary tree, each node can have at most two children, referred to as the left child and the right child.
# Binary trees are often used in scenarios where hierarchical data needs to be represented, such as in expression trees or decision trees.

# In a binary search tree (BST), the left child of a node contains a value less than its parent node, and the right child contains a value greater than its parent node.
# This property allows for efficient searching, insertion, and deletion operations, with average time complexities of O(log n) for balanced trees.
# BSTs are commonly used in applications that require fast lookups, such as in databases and indexing systems.

# Tries are another type of tree structure that is particularly useful for storing and retrieving strings or sequences of characters.
# Tries are also known as prefix trees because they take advantage of common prefixes in the stored strings to optimize space and search time.
# Each node in a trie represents a single character, and the path from the root to a leaf node represents a complete string.
# Tries are commonly used in applications such as autocomplete systems, spell checkers, and IP routing.

# An example of a trie storing the words "cat", "car", and "dog":
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current_node = self.root
        for char in word:
            if char not in current_node.children:
                current_node.children[char] = TrieNode()
            current_node = current_node.children[char]
        current_node.is_end_of_word = True

    def search(self, word):
        current_node = self.root
        for char in word:
            if char not in current_node.children:
                return False
            current_node = current_node.children[char]
        return current_node.is_end_of_word
    
# Example usage:
trie = Trie()
trie.insert("cat")
trie.insert("car")
trie.insert("dog") 

print(trie.search("cat"))  # Output: True
print(trie.search("car"))  # Output: True
print(trie.search("dog"))  # Output: True
print(trie.search("cow"))  # Output: False