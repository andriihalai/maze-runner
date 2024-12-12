import networkx as nx
import matplotlib.pyplot as plt
import random
import math
from CarAgent import CarAgent
from KnowledgeBase import KnowledgeBase


def remove_random_edges(G, num_edges_to_remove: int):
    edges = list(G.edges())
    if (len(edges) < num_edges_to_remove):
        num_edges_to_remove = len(edges)
    removed_edges = 0

    while removed_edges < num_edges_to_remove:
        edge_to_remove = random.choice(edges)

        G.remove_edge(*edge_to_remove)

        if nx.is_connected(G):
            removed_edges += 1
            edges.remove(edge_to_remove)
        else:
            G.add_edge(*edge_to_remove)


def generate_graph(num_vertices=25, num_edges_to_remove=0):
    n_rows = math.isqrt(num_vertices)
    n_cols = math.ceil(num_vertices / n_rows)

    G = nx.grid_2d_graph(n_rows, n_cols)

    extra_nodes = n_rows * n_cols - num_vertices
    if extra_nodes > 0:
        nodes_to_remove = [(i, j) for i in range(n_rows)
                           for j in range(n_cols)][-extra_nodes:]
        G.remove_nodes_from(nodes_to_remove)

    remove_random_edges(G, num_edges_to_remove)

    return G


graph = generate_graph(25, 12)
# graph = nx.Graph()
# graph.add_edge((0, 3), (0, 2))
# graph.add_edge((0, 2), (0, 1))
# graph.add_edge((0, 1), (0, 0))
# graph.add_edge((0, 0), (1, 0))
# graph.add_edge((1, 0), (2, 0))
# graph.add_edge((2, 0), (2, 1))
# graph.add_edge((2, 1), (2, 2))
# graph.add_edge((2, 2), (2, 3))
# graph.add_edge((0, 2), (1, 2))
# graph.add_edge((1, 2), (1, 3))
start = (0, 1)
target = (2, 3)
kb = KnowledgeBase(start, target)
agent = CarAgent(graph, kb)
pos = dict((n, n) for n in graph.nodes())
node_colors = [
    "red" if node == start else "blue" if node == target else "none"
    for node in graph.nodes()
]
nx.draw(graph, pos, with_labels=True,
        linewidths=1, node_color=node_colors, font_size=15)

try:
    agent.run()
except IndexError:
    print("IndexError")
plt.show()
