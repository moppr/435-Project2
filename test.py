from node import Node
from graph import Graph
from graph_search import GraphSearch
from main import *
import random

if __name__ == "__main__":
    sys.setrecursionlimit(256)
    for _ in range(0):
        random_weighted = create_random_complete_weighted_graph(10)
        print(random_weighted, "\n")
        linked_weighted = create_linked_list(10, True)
        print(linked_weighted, "\n")

    l = create_random_complete_weighted_graph(10)
    r = create_linked_list(10, True)
    print(l)
    dijkstras_random_weighted(l)
