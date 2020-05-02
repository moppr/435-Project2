from node import Node
from graph import Graph
from graph_search import GraphSearch
from main import *
import random

if __name__ == "__main__":
    random_dag = create_random_dag_iter(10, 1)
    print(random_dag)
    nodes = random_dag.get_all_nodes()
    while (node1 := nodes.pop()) and not node1.edges:
        if not nodes:
            node1 = None
            raise ValueError("Couldn't find a node with any edges to cut")
    node2 = node1.edges.copy().pop()
    print(f"\ncutting edge from {node1.value} to {node2.value}\n")
    random_dag.remove_directed_edge(node1, node2)
    print(random_dag)
