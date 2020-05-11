from functools import *


@total_ordering
class Node:
    """Node of a graph object that stores a value as a means of distinguishing ID."""

    def __init__(self, value):
        self.value = value
        self.edges = {}

    def __str__(self):
        # Unlike graph.__str__(), edges is not being sorted because the order of edge generation is
        # necessary to understand the trace of how searches and traversals generate their outputs.
        return f"{self.value}: {[(node.value, self.edges[node]) for node in self.edges]}"

    def __eq__(self, other):
        return self.value == other.value

    def __lt__(self, other):
        return self.value < other.value

    def __hash__(self):
        # Since __eq__ was defined, __hash__ is necessary to store Node objects
        # in the set being used to represent the adjacency list.
        return hash(self.value)

    def add(self, other, weight=0):
        self.edges[other] = weight

    def remove(self, other):
        if other in self.edges:
            self.edges.pop(other)
