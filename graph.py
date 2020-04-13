from node import Node


class Graph:
    """Undirected unweighted graph implementation using an adjacency list."""

    def __init__(self):
        self.adjacency_list = set()

    def __str__(self):
        result = ""
        for node in sorted(self.get_all_nodes()):
            print('e', node)
            result += f"{str(node)}\n"
        return result[:-1]

    def add_node(self, value):
        self.adjacency_list.add(Node(value))

    def add_undirected_edge(self, first, second):
        self._check_node_validity((first, second))
        # For the time being, not allowing nodes to have edges to themselves.
        if first == second:
            return

        first.add(second)
        second.add(first)

    def remove_undirected_edge(self, first, second):
        self._check_node_validity((first, second))

        first.remove(second)
        second.remove(first)

    def get_all_nodes(self):
        return self.adjacency_list.copy()

    def _check_node_validity(self, nodes):
        for node in nodes:
            if node not in self.adjacency_list:
                raise ValueError(f"Node {node} does not currently exist in the graph")
