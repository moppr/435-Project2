from directedgraph import DirectedGraph
from weightednode import WeightedNode


class WeightedGraph(DirectedGraph):
    """Modification of DirectedGraph to support edges with weights."""

    def add_node(self, value):
        node = WeightedNode(value)
        self.adjacency_list[node] = node

    def add_weighted_edge(self, first, second, weight):
        self._check_node_validity((first, second))
        if first == second:
            return

        first.add(second, weight)
