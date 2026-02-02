# There are two common ways to implement graphs in code: using adjacency matrices and adjacency lists.

# Adjacency Matrix:
# An adjacency matrix is a two-dimensional list in which the rows and columns represent the graphs vertices.
# The values in the matrix represent the edges or connections between the nodes.

#For example, if you have a matrix stored in variable matrix,
matrix = [
    [0, 1, 0, 0],
    [1, 0, 1, 1],
    [0, 1, 0, 0],
    [0, 1, 0, 0]
]

# In this example, the matrix represents a graph with four nodes (0, 1, 2, 3).
# A value of 1 indicates an edge between the nodes, while a value of 0 indicates no edge.
# There are edges between nodes 1 & 0, 1 & 2, and 1 & 3.

# If the graph is unweighted, the values in the matrix are typically 0 (no edge) or 1 (edge exists).
# If the graph is weighted, the values can represent the weights of the edges (e.g., distances, costs).
# One of the great advantages of matrices is that checking if there is an edge between two nodes takes constant time O(1) since you can directly access the matrix cell corresponding to those nodes.
# However, adjacency matrices can be inefficient in terms of space for sparse graphs (graphs with relatively few edges compared to the number of nodes) since they require O(V^2) space, where V is the number of vertices.

# Another way to represent graphs is through adjacency lists.
# There are two ways to implement adjacency lists: using dictionaries or using arrays.
# Adjacency lists are more space efficient that matricies, they have a O(V + E) space complexity, where V is the number of vertices and E is the number of edges.
# Its also efficient for finding all neightbor nodes, since this op only requires accessing the list associated to the node
# However, the time complexity for checking if there is an edge between two nodes is O(N) in the worst case, where N is the number of neighbors of a node.
# Which makes it less efficient than adjacency matrices for this specific operation.

# It may be easier to think of matrices as being for identifying if an edge exists between two nodes quickly,
# while adjacency lists are better suited for iterating over all neighbors of a node efficiently.

# Example of a simple undirected graph using an adjacency list representation
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Alternatively, we could implement it as a 2D list
adjacency_list = [
    ['B', 'C'],    # Neighbors of node 0 (A)
    ['A', 'D', 'E'],  # Neighbors of node 1 (B)
    ['A', 'F'],    # Neighbors of node 2 (C)
    ['B'],         # Neighbors of node 3 (D)
    ['B', 'F'],    # Neighbors of node 4 (E)
    ['C', 'E']     # Neighbors of node 5 (F)
]

