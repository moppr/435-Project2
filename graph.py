from node import Node


class Graph:
    """Undirected unweighted graph implementation using an adjacency list."""

    def __init__(self):
        self.adjacency_list = {}

    def __str__(self):
        result = ""
        for node in sorted(self.get_all_nodes()):
            result += f"{str(node)}\n"
        return result[:-1]

    def add_node(self, value):
        node = Node(value)
        self.adjacency_list[node] = node

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
        return set(self.adjacency_list)

    def get_node(self, value):
        if isinstance(value, Node):
            return self.adjacency_list[value]
        return self.adjacency_list[Node(value)]

    def _check_node_validity(self, nodes):
        for node in nodes:
            if node not in self.adjacency_list:
                raise ValueError(f"Node {node} does not currently exist in the graph")
