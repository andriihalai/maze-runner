import networkx as nx
import math
import random


class KnowledgeBase:
    def __init__(self, current_node: tuple[int, int],
                 target_node: tuple[int, int]):
        self.G = nx.Graph()
        self.deadlock = set()
        self.visited = [current_node]
        self.current_node = current_node
        self.target_node = target_node

    def addEdges(self, edges):
        for edge in edges:
            self.G.add_edge(edge[0], edge[1])

    def findDeadlocks(self):
        self.deadlock = [n for n, d in self.G.degree() if d == 1]

    def getClosestNode(self):
        closest_nodes = []
        min_distance = float('inf')

        nodes = self.G.nodes
        if self.target_node in nodes:
            return self.target_node

        nodes = [n for n in self.G.nodes if n not in list(self.deadlock)]
        nodes = [n for n in nodes if n not in self.visited]

        for node in nodes:
            d = self.calculate_distance(node, self.target_node)

            if d < min_distance:
                min_distance = d
                closest_nodes = [node]
            elif d == min_distance:
                closest_nodes.append(node)

        closest = random.choice(closest_nodes)
        return closest

    def get_next_node(self):
        node = self.getClosestNode()
        # print("Closest: ", node)
        path = nx.shortest_path(self.G, self.current_node, node)
        return path[1]

    def calculate_distance(self, src: tuple[int, int], dest: tuple[int, int]):
        x1, y1 = src
        x2, y2 = dest
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    def update_current_node(self, node):
        self.current_node = node
        self.visited.append(node)

    def should_continue(self):
        if (self.current_node == self.target_node):
            return False
        else:
            return True
