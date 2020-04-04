from graph import Graph
from node import Node
import random


def create_random_unweighted_graph_iter(n):
    """Return a graph of n nodes with randomly assigned unweighted, undirected edges."""
    graph = Graph()
    for number in random.sample(range(n), n):
        graph.add_node(number)

    nodes = graph.get_all_nodes()

    for node in nodes:
        # pick up to half of the other nodes to connect to
        num_edges = int(random.random() * .5 * len(nodes))
        for other in random.sample(nodes, num_edges):
            graph.add_undirected_edge(node, other)

    return graph


def create_linked_list(n):
    """Return a graph of n nodes that represent a linked list.

    Note - the prompt implies that this is a directed linked list, but discussion
    on Slack has suggested that undirected is preferred to be consistent with part a,
    so undirected is implemented here.
    """
    graph = Graph()
    for number in range(10):
        graph.add_node(number)

        if number == 0:
            continue

        graph.add_undirected_edge(Node(number), Node(number-1))

    return graph


if __name__ == "__main__":
    random_unweighted_graph = create_random_unweighted_graph_iter(10)
    print(random_unweighted_graph, "\n")
    linked_list = create_linked_list(10)
    print(linked_list)

