from graph import Graph


class DirectedGraph(Graph):

    def add_directed_edge(self, first, second):
        self._check_node_validity((first, second))
        if first == second:
            return

        if second not in first.incoming_connections:
            first.add(second)
            second.add_connections(first)

    def remove_directed_edge(self, first, second):
        self._check_node_validity((first, second))

        first.remove(second)
        second.remove_connections(first)
