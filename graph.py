from node import Node


class Graph:
    """Undirected unweighted graph implementation using an adjacency list."""

    def __init__(self):
        """Init with blank adjacency list as dictionary."""
        self.adjacency_list = {}

    def __str__(self):
        """Return adjacency list to represent graph as a string."""
        result = ""
        for node in sorted(self.get_all_nodes()):
            result += f"{str(node)}\n"
        return result[:-1]

    def add_node(self, value):
        """Create new node with specified value and add to adjacency list."""
        node = Node(value)
        self.adjacency_list[node] = node

    def add_undirected_edge(self, first, second):
        """Create adjacency between nodes first and second, provided they exist."""
        self._check_node_validity((first, second))
        if first == second:
            return

        self.adjacency_list[first].add(second)
        self.adjacency_list[second].add(first)

    def remove_undirected_edge(self, first, second):
        """Remove adjacency between nodes first and second, provided they exist."""
        self._check_node_validity((first, second))

        self.adjacency_list[first].remove(second)
        self.adjacency_list[second].remove(first)

    def get_all_nodes(self):
        """Return set containing all nodes present in adjacency list."""
        return set(self.adjacency_list)

    def get_node(self, value):
        """Return a node object given its value.

        Note - this is useful because nodes with equivalent values have equivalent hashes,
        allowing for ease of testing membership within the graph's adjacency list. However,
        new Node objects do not automatically populate with the same list of edges as the
        members of the graph's adjacency list, so this function retrieves the node object
        that does contain the proper edges given its value.
        """
        return self.adjacency_list[Node(value)]

    def _check_node_validity(self, nodes):
        """Raise error if any node in nodes does not exist in the adjacency list."""
        for node in nodes:
            if node not in self.adjacency_list:
                raise ValueError(f"Node {node} does not currently exist in the graph")
