# Traversing the data structure is a process of visiting all the nodes in a specific order.
# Two common methods for traversing graphs are Depth-First Search (DFS) and Breadth-First Search (BFS).
# They are used to traverse the data structure, they define the order in which the nodes should be visited to make sure that none of them is skipped.

# Breadth-First Search (BFS):
# BFS is an algorithm that visits all neighboring nodes before moving to the next level in the graph.
# It can be used to find the shortest parth between two nodes in an unweighted graph because it analyzes all the nodes at each level, so it findes the parth with fewest edges first.

# This algorithm is commonly implemented using a queue data structure to keep track of the nodes that have been visited and the nodes that are yet to be explored.
# Queues follow the First In First Out (FIFO) principle, meaning that the first node added to the queue will be the first one to be processed.

# The algorithm works as follows:
# 1. You start at a specified node (the starting node) and mark it as visited and add to the queue.
# 2. While the queue is not empty, you remove the first node from the queue (the current node) and visit all its unvisited neighbors.
# 3. Each unvisited neighbor is marked as visited and added to the queue.

# Since BFS stores a queue in memory, and this queue may have a large number of nodes, the space requirements can be large
# This is especially true for graphs with a large number of nodes on the same level.

# Lets see and example of BFS applied to a tree structure:
from collections import deque

def bfs(graph, start):
    visited = set()          # Set to keep track of visited nodes
    queue = deque([start])  # Initialize a queue with the starting node
    visited.add(start)      # Mark the starting node as visited

    while queue:
        current_node = queue.popleft()  # Dequeue a node from the front of the queue
        print(current_node)              # Process the current node (e.g., print it)

        # Get all unvisited neighbors of the current node
        for neighbor in graph.get(current_node, []):
            if neighbor not in visited:
                visited.add(neighbor)    # Mark neighbor as visited
                queue.append(neighbor)   # Enqueue the neighbor

# Example graph represented as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}   

# Perform BFS starting from node 'A'
bfs(graph, 'A')

# Depth-First Search (DFS):
# DFS follows each branch as deep as possible before backtracking.
# You can imagine this as picking between three tunnels, and going down one tunnel until you reach the end, then backtracking to the last junction and picking another tunnel to explore.
# DFS is commonly used to solve problems that require a single solution, detecting cycles in a graph, and finding connected components.
# This algorithm can be implemented using recursion or a stack to keep track of visited nodes.
# Stacks follow the Last In First Out (LIFO) principle, meaning that the last node added to the stack will be the first one to be processed.

# The algorithm works as follows:
# 1. You start at a specific node, mark it as visited and push it onto the stack.
# 2. While the stack is not empty, you pop a node from the stack and then mark all of its unvisited neighbors as visited and push them onto the stack.
# 3. This process continues until all nodes have been visited.

# One of the limitations of DFS is that its not always guaranteed to find the shortest path between two nodes in an unweighted graph.
# However, it can be more memory efficient than BFS, especially for graphs with a large branching factor.

# Lets see an example of DFS applied to a tree structure:
def dfs(graph, start, visited=None): # Using visited=None to avoid mutable default argument
    if visited is None:
        visited = set()          # Initialize the visited set on the first call
    visited.add(start)          # Mark the current node as visited
    print(start)                # Process the current node (e.g., print it)

    # Recur for all unvisited neighbors of the current node
    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# Example graph represented as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Perform DFS starting from node 'A'
dfs(graph, 'A')