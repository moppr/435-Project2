import random
from node import Node
from graph import Graph

if __name__ == "__main__":
    g = Graph()
    g.add_node(3)
    g.add_node(4)
    g.add_node(5)
    g.add_undirected_edge(Node(3), Node(5))
    print(g)
    print()
    print(Node(3))
    print(g.get_node(3))


