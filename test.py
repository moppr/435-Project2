from node import Node
from graph import Graph
from graph_search import GraphSearch
from main import *
import random

if __name__ == "__main__":
    sys.setrecursionlimit(256)
    for _ in range(10):
        random_dag = create_random_dag_iter(8)
        print(random_dag)
        mdfs_iter_random_dag(random_dag)
        kahns_iter_random_dag(random_dag)
        print()
