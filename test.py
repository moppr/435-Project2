from node import Node
from graph import Graph
from graph_search import GraphSearch
from main import *
import random

if __name__ == "__main__":
    sys.setrecursionlimit(256)
    n = 3
    random_grid = create_random_grid_graph(n)
    source, dest = random_grid.get_node(GridNode(0, 0)), random_grid.get_node(GridNode(n-1, n-1))
    a_star_random(random_grid, source, dest)
    print(random_grid)
