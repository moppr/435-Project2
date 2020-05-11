from graph import Graph
from directedgraph import DirectedGraph
from weightedgraph import WeightedGraph
from node import Node
from graph_search import GraphSearch
from topsort import TopSort
from datetime import *
import random
import sys


sys.setrecursionlimit(2048)


def create_random_graph_iter(num_nodes, connectivity, graph):
    if connectivity > 1:
        raise ValueError(f"Cannot attempt to connect to more than every other node "
                         f"(Connectivity of {connectivity} was greater than 1)")

    if isinstance(graph, DirectedGraph):
        mode = "dag"
    else:
        mode = "unweighted"

    for number in random.sample(range(num_nodes), num_nodes):
        graph.add_node(number)

    for node in (nodes := graph.get_all_nodes()):
        # Choose a ratio of up to connectivity of the other nodes to connect to.
        num_edges = int(random.random() * connectivity * len(nodes))
        for other in random.sample(nodes, num_edges):
            if mode == "unweighted":
                graph.add_undirected_edge(node, other)
            elif mode == "dag":
                graph.add_directed_edge(node, other)

    return graph


def create_random_unweighted_graph_iter(num_nodes, connectivity=.5):
    return create_random_graph_iter(num_nodes, connectivity, Graph())


def create_random_dag_iter(num_nodes, connectivity=.75):
    return GraphSearch.cut_cycles(create_random_graph_iter(num_nodes, connectivity, DirectedGraph()))


def create_random_complete_weighted_graph(num_nodes, weight_limit=10):
    if weight_limit < 1:
        raise ValueError(f"Weight limit {weight_limit} must be at least 1")

    graph = WeightedGraph()

    for number in random.sample(range(num_nodes), num_nodes):
        graph.add_node(number)

    nodes = graph.get_all_nodes()
    for node in nodes:
        for other in nodes:
            graph.add_weighted_edge(node, other, random.randint(1, weight_limit))

    return graph


def create_linked_list(num_nodes, weighted=False):
    # (Part 3) The prompt implies that this is a directed linked list, but discussion on Slack has suggested
    # that undirected is preferred to be consistent with part a, so undirected is implemented here.
    if weighted:
        graph = WeightedGraph()
    else:
        graph = Graph()

    for number in range(num_nodes):
        graph.add_node(number)

    for number in range(num_nodes-1):
        if weighted:
            graph.add_weighted_edge(graph.get_node(number), graph.get_node(number+1), 1)
        else:
            graph.add_undirected_edge(graph.get_node(number), graph.get_node(number+1))

    return graph


def dijkstras(start):
    distances = {start: 0}
    visited = set()
    node = start
    while node and distances[node] < 999:
        visited.add(node)
        for other in node.edges:
            if other not in visited:
                new_dist = distances[node] + node.edges[other]
                if other not in distances or new_dist < distances[other]:
                    distances[other] = new_dist

        node = None
        min_seen = 999
        for other in distances:
            if other not in visited and distances[other] <= min_seen:
                min_seen = distances[other]
                node = other

    return distances


def list_print(lst):
    if lst:
        return [item.value for item in lst]


def dict_print(dic):
    if dic:
        return {item.value : dic[item] for item in dic}


def bft_rec_linked_list(graph):
    print("bft_rec: ", list_print(GraphSearch.bft_rec(graph)))


def bft_iter_linked_list(graph):
    print("bft_iter:", list_print(GraphSearch.bft_iter(graph)))


def mdfs_iter_random_dag(graph):
    print("mdfs:", list_print(TopSort.mdfs(graph)))


def kahns_iter_random_dag(graph):
    print("kahns:", list_print(TopSort.kahns(graph)))


def dijkstras_random_weighted(graph):
    print("dijkstras_random:", dict_print(dijkstras(graph.get_node(0))))


def dijkstras_linked_weighted(graph):
    print("dijkstras_linked:", dict_print(dijkstras(graph.get_node(0))))


if __name__ == "__main__":
    large_linked_list = create_linked_list(10000)
    small_linked_list = create_linked_list(100)
    random_dag = create_random_dag_iter(1000)
    # No instruction was provided for what to call dijkstra's on - using size 100 for now
    random_weighted = create_random_complete_weighted_graph(100)
    linked_weighted = create_linked_list(100, True)

    try:
        bft_rec_linked_list(large_linked_list)
    except RecursionError:
        print("10000 nodes was too large for recursive BFT. Attempting 100...")
        bft_rec_linked_list(small_linked_list)

    bft_iter_linked_list(large_linked_list)
    mdfs_iter_random_dag(random_dag)
    kahns_iter_random_dag(random_dag)
    dijkstras_random_weighted(random_weighted)
    dijkstras_linked_weighted(linked_weighted)
