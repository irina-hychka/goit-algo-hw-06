import heapq
import networkx as nx
import matplotlib.pyplot as plt
from task1 import create_scooter_graph

def dijkstra_find_shortest_path(graph_dict, start_node):
    """
    Dijkstra's algorithm implementation for finding the shortest paths in a graph.

    Parameters:
        graph_dict (dict): Graph represented as an adjacency dictionary.
        start_node (str): Starting node for path calculation.

    Returns:
        tuple: (distances, previous_nodes)
            - distances: dict with shortest distance from start_node to each node
            - previous_nodes: dict to reconstruct the path to each node
    """
    if start_node not in graph_dict:
        raise ValueError(f"Start node '{start_node}' not found in graph.")

    distances = {node: float('inf') for node in graph_dict}
    distances[start_node] = 0
    previous_nodes = {node: None for node in graph_dict}
    priority_queue = [(0, start_node)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, edge_data in graph_dict[current_node].items():
            weight = edge_data.get('weight', 1)  # Default to 1 if no weight specified
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances, previous_nodes

def find_shortest_path_helper(previous_nodes, start_node, end_node):
    """
    Helper function to reconstruct the shortest path from start_node to end_node.

    Parameters:
        previous_nodes (dict): Previous nodes map from Dijkstra's output
        start_node (str): Starting node
        end_node (str): Target node

    Returns:
        list: Path as a list of node names, or None if no path exists
    """
    path = []
    current = end_node

    while current is not None:
        path.insert(0, current)
        if current == start_node:
            break
        current = previous_nodes.get(current)

    if path and path[0] == start_node:
        return path
    return None

# --- Main Execution ---

# Step 1: Create the graph with weights based on trip duration
G, _ = create_scooter_graph()

# Add weights to the graph based on avg_duration attribute
for u, v, data in G.edges(data=True):
    G[u][v]['weight'] = data['avg_duration']

# Step 2: Convert to dictionary for manual Dijkstra
graph_dict = nx.to_dict_of_dicts(G)

# Choose starting station
start_station = "Central Square"
distances, prev_nodes = dijkstra_find_shortest_path(graph_dict, start_station)

print(f"\nShortest paths from '{start_station}':\n")
for target in sorted(G.nodes):
    path = find_shortest_path_helper(prev_nodes, start_station, target)
    distance = distances.get(target, float('inf'))
    if path:
        print(f"  - To {target}: {' -> '.join(path)} (Duration: {distance} min)")
    else:
        print(f"  - To {target}: No path found")

# Step 3: Visualize the weighted graph
plt.figure(figsize=(12, 8))
pos = nx.spring_layout(G, seed=42)
nx.draw_networkx_nodes(G, pos, node_color='lightblue', node_size=2200)
nx.draw_networkx_labels(G, pos, font_size=10, font_weight='bold')
nx.draw_networkx_edges(G, pos, edge_color='gray')
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels={k: f"{v} min" for k, v in edge_labels.items()}, font_size=8)

plt.title("E-Scooter Network with Travel Durations")
plt.axis('off')
plt.tight_layout()
plt.show()
