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
        # Mapping node objects to themselves seems odd, but is done to be able to
        # access the node object (which contains the adjacency list) in constant
        # time while only knowing its value.
        self.adjacency_list[node] = node

    def add_undirected_edge(self, first, second):
        self._check_node_validity((first, second))
        # For the time being, not allowing nodes to connect to themselves.
        if first == second:
            return

        self.adjacency_list[first].add(second)
        self.adjacency_list[second].add(first)

    def remove_undirected_edge(self, first, second):
        self._check_node_validity((first, second))

        self.adjacency_list[first].remove(second)
        self.adjacency_list[second].remove(first)

    def get_all_nodes(self):
        return set(self.adjacency_list)

    def get_node(self, value):
        # This is useful because nodes with equivalent values have equivalent hashes,
        # allowing for ease of testing membership within the graph's adjacency list. However,
        # new Node objects do not automatically populate with the same list of edges as the
        # members of the graph's adjacency list, so this function retrieves the node object
        # that does contain the proper edges given its value.
        return self.adjacency_list[Node(value)]

    def _check_node_validity(self, nodes):
        for node in nodes:
            if node not in self.adjacency_list:
                raise ValueError(f"Node {node} does not currently exist in the graph")
