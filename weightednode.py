from node import Node


class WeightedNode(Node):
    """Modification of Node to store weights of edges in a dictionary."""

    def __init__(self, value):
        self.value = value
        self.edges = {}

    def __str__(self):
        # Unlike graph.__str__(), edges is not being sorted because the order of edge generation is
        # necessary to understand the trace of how searches and traversals generate their outputs.
        return f"{self.value}: {[(node.value, self.edges[node]) for node in self.edges]}"

    def add(self, other, weight=0):
        self.edges[other] = weight

    def remove(self, other):
        if other in self.edges:
            self.edges.pop(other)