# NetworkX is a Python package for the creation, manipulation, and study of the structure, dynamics, and functions of complex networks. It provides tools for working with graphs and networks, including algorithms for graph analysis, visualization, and more.

import networkx as nx
import matplotlib.pyplot as plt


G = nx.Graph()
G.add_node(1)
G.add_nodes_from([2, 3])
G.add_edge(1, 2)
G.add_edges_from([(1, 3), (2, 3)])

print(G.nodes())  # Output: [1, 2, 3]
print(G.edges())  # Output: [(1, 2), (1, 3), (2, 3)]

nx.draw(G, with_labels=True)
plt.show()

# These are some of the basic functions of NetworkX, but the library offers a wide range of functionalities for working with graphs and networks, including algorithms for shortest paths, centrality measures, community detection, and more.
# Note that nodes can be any hashable object, not just integers.
# Hashable objects are: Strings, Numbers, Tuples, Sets, Frozensets, and more. Lists and dictionaries are not hashable because they are mutable.
# The definition of hashable objects can be found here: https://docs.python.org/3/glossary.html#term-hashable
