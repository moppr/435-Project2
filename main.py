from graph import Graph
from directedgraph import DirectedGraph
from node import Node
from graph_search import GraphSearch
import random


def create_random_graph_iter(num_nodes, connectivity, graph):
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


def create_random_dag_iter(num_nodes, connectivity=.67):
    # TODO: Cut cycles
    return create_random_graph_iter(num_nodes, connectivity, DirectedGraph())


def create_linked_list(num_nodes):
    # The prompt implies that this is a directed linked list, but discussion on Slack has suggested
    # that undirected is preferred to be consistent with part a, so undirected is implemented here.
    graph = Graph()
    for number in range(num_nodes):
        graph.add_node(number)

        if number == 0:
            continue

        graph.add_undirected_edge(Node(number), Node(number-1))

    return graph


def list_print(lst):
    if lst:
        return [item.value for item in lst]


def bft_rec_linked_list(graph):
    print("bft_rec: ", list_print(GraphSearch.bft_rec(graph)))


def bft_iter_linked_list(graph):
    print("bft_iter:", list_print(GraphSearch.bft_iter(graph)))


if __name__ == "__main__":
    large_linked_list = create_linked_list(10000)
    small_linked_list = create_linked_list(100)

    try:
        bft_rec_linked_list(large_linked_list)
    except RecursionError:
        print("10000 nodes was too large for recursive BFT. Attempting 100...")
        bft_rec_linked_list(small_linked_list)

    bft_iter_linked_list(large_linked_list)
