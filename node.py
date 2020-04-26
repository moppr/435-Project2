from functools import *
from graph_search import GraphSearch


@total_ordering
class Node:
    """Node of a graph object that stores a value as a means of distinguishing ID"""

    def __init__(self, value):
        self.value = value
        self.edges = set()
        # Nodes don't actually connect to themselves but marking them as such prevents
        # these false connections from happening later on.
        self.incoming_connections = {self}

    def __str__(self):
        # Unlike graph.__str__(), edges is not being sorted because the order of edge generation is
        # necessary to understand the trace of how searches and traversals generate their outputs.
        return f"{self.value}: {[node.value for node in self.edges]}"

    def __eq__(self, other):
        return self.value == other.value

    def __lt__(self, other):
        return self.value < other.value

    def __hash__(self):
        # Since __eq__ was defined, __hash__ is necessary to store Node objects
        # in the set being used to represent the adjacency list.
        return hash(self.value)

    def add(self, other):
        self.edges.add(other)

    def remove(self, other):
        if other in self.edges:
            self.edges.remove(other)

    def add_connections(self, incoming):
        self.incoming_connections.update(incoming.incoming_connections)
        for other in self.edges:
            other.add_connections(self)  # Using self is the same as using incoming, theoretically.

    def remove_connections(self, incoming):
        for other in incoming.incoming_connections:  # Members are guaranteed to be in self's incoming.
            # Not the most efficient thing in the world, but I couldn't find a better way of determining
            # if a given connection should be removed or not because I'm not tracking the source(s) of
            # each individual connection, and only one source is being removed at a time.
            if not (search := GraphSearch.dfs_iter(other, self)):
                self.incoming_connections.remove(other)
