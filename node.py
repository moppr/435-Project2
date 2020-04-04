from functools import *


@total_ordering
class Node:
    """Node of a graph object that stores a value."""

    def __init__(self, value):
        """Init with a given value."""
        self.value = value

    def __str__(self):
        """Return value to represent node as a string."""
        return str(self.value)

    def __eq__(self, other):
        """Return equality of value attributes of Node objects."""
        return self.value == other.value

    def __lt__(self, other):
        """Return inequality of value attributes of Node objects."""
        return self.value < other.value

    def __hash__(self):
        """Return hash of value attributes of Node objects.

        Since __eq__ was defined, this is necessary to store Node objects
        as keys in the dictionary being used to represent the adjacency list.
        """
        return hash(self.value)
