from node import Node
from graph import Graph
from graph_search import GraphSearch
from main import *
import random

if __name__ == "__main__":
    random_dag = create_random_dag_iter(10)
    print(random_dag)
