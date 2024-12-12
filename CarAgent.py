import networkx as nx
from KnowledgeBase import KnowledgeBase


class CarAgent:
    def __init__(self, G: nx.Graph, kb: KnowledgeBase) -> None:
        self.current_node = kb.current_node
        self.target_node = kb.target_node
        self.kb = kb
        self.G = G

    def investigateGraph(self):
        self.kb.addEdges(self.G.edges(self.current_node))

        neighbors = self.G.neighbors(self.current_node)
        for n in neighbors:
            eds = list(self.G.edges(n))

            self.kb.addEdges(eds)
            if len(eds) == 1:
                self.kb.deadlock.add(n)

    def run(self):
        print("current node: ", self.current_node)
        self.investigateGraph()
        while (self.kb.should_continue()):
            next_node = self.kb.get_next_node()
            self.current_node = next_node
            self.kb.update_current_node(next_node)
            self.investigateGraph()
            print("current node: ", self.current_node)
        print("Destination reached")

    def test(self):
        self.investigateGraph()
        print(self.kb.G.edges())
        print(self.kb.G.nodes)
        print(self.kb.getClosestNode())
        print(self.kb.get_next_node())
