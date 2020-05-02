from graph import Graph


class DirectedGraph(Graph):

    def add_directed_edge(self, first, second):
        self._check_node_validity((first, second))
        if first == second:
            return

        first.add(second)

    def remove_directed_edge(self, first, second):
        self._check_node_validity((first, second))

        first.remove(second)
