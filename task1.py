import networkx as nx
import matplotlib.pyplot as plt

def create_scooter_graph():
    # Create an undirected graph to represent scooter rental stations
    G = nx.Graph()

    # Define the stations (nodes)
    stations = [
        "Central Square",
        "Central District Hospital",
        "Stadium",
        "Railway Station",
        "Machinery Plant District",
        "Market"
    ]
    G.add_nodes_from(stations)

    # Define the movements (edges) between stations with attributes:
    # Number of trips and average duration (in minutes)
    edges = [
        ("Central Square", "Stadium", {"trips": 320, "avg_duration": 7}),
        ("Central Square", "Railway Station", {"trips": 20, "avg_duration": 24}),
        ("Central Square", "Central District Hospital", {"trips": 30, "avg_duration": 5}),
        ("Railway Station", "Machinery Plant District", {"trips": 10, "avg_duration": 12}),
        ("Machinery Plant District", "Stadium", {"trips": 30, "avg_duration": 15}),
        ("Central District Hospital", "Stadium", {"trips": 40, "avg_duration": 15}),
        ("Central Square", "Market", {"trips": 50, "avg_duration": 20}),
        ("Machinery Plant District", "Market", {"trips": 8, "avg_duration": 24})
    ]
    G.add_edges_from(edges)

    return G, edges


if __name__ == "__main__":
    # Call Graph Creation
    G, edges = create_scooter_graph()

    # Visualize the graph
    plt.figure(figsize=(12, 8))
    pos = nx.spring_layout(G, seed=42)

    # Draw nodes and labels
    nx.draw_networkx_nodes(G, pos, node_size=2000, node_color="lightgreen")
    nx.draw_networkx_labels(G, pos, font_size=10, font_weight="bold")

    # Draw edges with labels showing number of trips
    nx.draw_networkx_edges(G, pos, edge_color="gray")
    edge_labels = {(u, v): f"{d['trips']} trips\n{d['avg_duration']} min"
                for u, v, d in G.edges(data=True)}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8)

    plt.title("E-Scooter Sharing Network (Zolotonosha)")
    plt.axis("off")
    plt.tight_layout()
    plt.show()

    # Graph Analysis
    num_nodes = G.number_of_nodes()
    num_edges = G.number_of_edges()
    degrees = dict(G.degree())

    num_nodes = G.number_of_nodes()
    num_edges = G.number_of_edges()
    degrees = dict(G.degree())
    most_used_edge = max(edges, key=lambda e: e[2]['trips'])
    central_node = max(degrees.items(), key=lambda x: x[1])

    print(f"Number of stations (nodes): {num_nodes}")
    print(f"Number of connections (edges): {num_edges}")
    print("\nNode degrees (number of direct connections):")
    for node, deg in degrees.items():
        print(f"{node}: {deg}")
    print("Most popular route:", most_used_edge)
    print("Most connected station:", central_node)
