from node import Node
from graph import Graph
from graph_search import GraphSearch
from main import *
import random

if __name__ == "__main__":
    random_unweighted_graph = create_random_unweighted_graph_iter(10)
    print(random_unweighted_graph, "\n")
    all_nodes = random_unweighted_graph.get_all_nodes()
    node1, node2 = all_nodes.pop(), all_nodes.pop()
    print(f"traveling from {node1.value} to {node2.value}")
    gs = GraphSearch()
    result = gs.dfs_rec(node1, node2)
    print("dfs_rec: ", list_print(result))
    result = gs.dfs_iter(node1, node2)
    print("dfs_iter:", list_print(result))
    result = gs.bft_rec(random_unweighted_graph)
    print("bft_rec: ", list_print(result))
    result = gs.bft_iter(random_unweighted_graph)
    print("bft_iter:", list_print(result))
