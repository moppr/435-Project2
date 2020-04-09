from graph import Graph
from node import Node
from graph_search import GraphSearch
import random


def create_random_unweighted_graph_iter(num_nodes):
    graph = Graph()
    for number in random.sample(range(num_nodes), num_nodes):
        graph.add_node(number)

    nodes = graph.get_all_nodes()

    for node in nodes:
        # choose up to half of the other nodes to connect to
        num_edges = int(random.random() * .5 * len(nodes))
        for other in random.sample(nodes, num_edges):
            graph.add_undirected_edge(node, other)

    return graph


def create_linked_list(num_nodes):
    # the prompt implies that this is a directed linked list, but discussion
    # on Slack has suggested that undirected is preferred to be consistent with part a,
    # so undirected is implemented here.
    graph = Graph()
    for number in range(num_nodes):
        graph.add_node(number)

        if number == 0:
            continue

        graph.add_undirected_edge(Node(number), Node(number-1))

    return graph


def list_print(lst):
    return [item.value for item in lst] if lst else None


if __name__ == "__main__":
    random_unweighted_graph = create_random_unweighted_graph_iter(10)
    print(random_unweighted_graph, "\n")
    # linked_list = create_linked_list(10)
    # print(linked_list, "\n")

    node1 = random_unweighted_graph.get_node(3)
    node2 = random_unweighted_graph.get_node(5)
    gs = GraphSearch()
    result = gs.dfs_rec(node1, node2)
    print("dfs_rec: ", list_print(result))
    result = gs.dfs_iter(node1, node2)
    print("dfs_iter:", list_print(result))
    # result = gs.bft_rec(random_unweighted_graph)
    # print(list_print(result))
