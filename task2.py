import networkx as nx
from task1 import create_scooter_graph

# Create the graph from task 1
G, edges = create_scooter_graph()

def dfs_search_path(graph: nx.Graph, start: str, goal: str) -> list | None:
    """
    Find a path from start to goal using Depth-First Search (DFS).

    Parameters:
        graph (nx.Graph): The graph to search in.
        start (str): The starting node.
        goal (str): The goal node.

    Returns:
        list: A list of nodes representing the DFS path, or None if no path exists.
    """
    stack = [(start, [start])]
    visited = {start}
    while stack:
        vertex, path = stack.pop()
        for neighbor in set(graph.neighbors(vertex)) - visited:
            if neighbor == goal:
                return path + [neighbor]
            visited.add(neighbor)
            stack.append((neighbor, path + [neighbor]))
    return None

def bfs_search_path(graph: nx.Graph, start: str, goal: str) -> list | None:
    """
    Find a path from start to goal using Breadth-First Search (BFS).

    Parameters:
        graph (nx.Graph): The graph to search in.
        start (str): The starting node.
        goal (str): The goal node.

    Returns:
        list: A list of nodes representing the BFS path, or None if no path exists.
    """
    queue = [(start, [start])]
    visited = {start}
    while queue:
        vertex, path = queue.pop(0)
        for neighbor in set(graph.neighbors(vertex)) - visited:
            if neighbor == goal:
                return path + [neighbor]
            visited.add(neighbor)
            queue.append((neighbor, path + [neighbor]))
    return None

# Define source and target nodes
start_node = "Central Square"
end_node = "Machinery Plant District"

# Find paths using both algorithms
dfs_route = dfs_search_path(G, start_node, end_node)
bfs_route = bfs_search_path(G, start_node, end_node)

# Display results
print(f"DFS path: {' → '.join(dfs_route) if dfs_route else 'No path found'}")
print(f"BFS path: {' → '.join(bfs_route) if bfs_route else 'No path found'}")

# Compare and explain the difference
print("\nComparison and Explanation:")

if dfs_route != bfs_route:
    print(
        "DFS explores paths deeply before backtracking, which may result in longer or suboptimal paths.\n"
        "BFS explores neighbors level-by-level and always finds the shortest path in terms of the number of steps."
    )
else:
    print(
        "In this case, DFS and BFS returned the same path. This may happen when the shortest path is also the first one explored by DFS."
    )
