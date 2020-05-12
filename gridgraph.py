from graph import Graph
from gridnode import GridNode


class GridGraph(Graph):
    """Modification of graph to support GridNodes."""

    def add_grid_node(self, x, y):
        node = GridNode(x, y)
        self.adjacency_list[node] = node

    def add_undirected_edge(self, first, second):
        self._check_node_validity((first, second))
        if first.is_neighbor(second):
            first.add(second)
            second.add(first)
