# Graphs are data structures used to represent the connections or relationships between objects or entities.
# They're often used to model networks, such as social networks, transportation systems, and communication networks.

#For example graphs can represent connections between users on a social media platform, or connections between cities on a road network.

# A graph is often represented as a collection of points or circles connected by lines
# The circles and lines represent the two main components of a graph: Nodes and Edges

# Nodes (or vertices) represent the objects or entities that are part of the network modeled by the graph.
# They could be users, products, stations, cities, or any other entities in the model

# Edges (or links) represent the connections or relationships between the nodes.
# They could represent friendships, transactions, routes, or any other type of relationship between the entities

# If two nodes are directly connected by an edge, they are called adjacent nodes or neighbors.
# There are different types of graphs, including directed and undirected graphs, weighted and unweighted graphs, and cyclic and acyclic graphs.

#Undirected Graphs: In an undirected graph, the edges have no direction.
# This means that the relationship between the nodes is bidirectional.
# For example, in a social network, if two users are friends, the friendship is mutual

#Directed Graphs: In a directed graph, the edges have a direction.
# This means that the relationship between the nodes is unidirectional.
# For example, in a Twitter-like social network, if one user follows another user, the relationship is one-way

# Weighted Graphs: In a weighted graph, the edges have a weight or cost associated with them.
# This weight could represent distance, time, or any other metric that quantifies the relationship between the nodes.
# For example, in a transportation network, the weight of an edge could represent the distance between two cities

# Vertex Labeled Graphs: In a vertex labeled graph, each node has a unique label or identifier associated with it.
# This label could be a name, number, or any other identifier that distinguishes the nodes from each other.
# For example, in a social network, each user could have a unique username or ID associated with their profile.

# Cyclic Graphs: In a cyclic graph, there are paths that start and end at the same node, forming a cycle.
# For example, in a transportation network, a cycle could represent a route that starts and ends at the same city.

# Acyclic Graphs: In an acyclic graph, there are no cycles.
# For example, a family tree is an acyclic graph, as there are no cycles in the relationships between family members.

# Edge Labeled Graphs: In an edge labeled graph, each edge has a unique label or identifier associated with it.
# This label could represent the type of relationship between the nodes or any other relevant information.
# For example, in a social network, the edges could be labeled to indicate whether the relationship is a friendship, a follow, or a block.

# Unweighted Graphs: In an unweighted graph, the edges do not have any weights or costs associated with them.
# This means that all edges are considered equal in terms of their relationship between the nodes.
# For example, in a simple social network, the edges could represent friendships without any additional information

# Disconnected Graphs: In a disconnected graph, there are nodes that are not connected to each other by any path.
# This means that there are separate components within the graph that are not connected to each other.
# For example, in a social network, there could be groups of users who are not connected

# Directed Acyclic Graphs (DAGs): A directed acyclic graph is a type of graph that has directed edges and contains no cycles.
# DAGs are often used to represent hierarchical structures, such as task scheduling, version control systems, and data processing pipelines.
# In a DAG, each edge has a direction, indicating the flow of information or dependencies between nodes.
# The absence of cycles ensures that there are no circular dependencies, allowing for a clear ordering of tasks or events.

# Example of a simple undirected graph using an adjacency list representation
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}
# Function to add an edge to the graph
def add_edge(graph, node1, node2):
    graph.setdefault(node1, []).append(node2)
    graph.setdefault(node2, []).append(node1)
# Function to display the graph
def display_graph(graph):
    for node, edges in graph.items():
        print(f"{node}: {', '.join(edges)}")
# Example usage
add_edge(graph, 'A', 'D')
display_graph(graph)