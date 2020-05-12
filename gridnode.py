from node import Node


class GridNode(Node):
    """Modification of Node to only have four cardinal neighbors and store location."""

    def __init__(self, x=0, y=0):
        self.x, self.y = x, y
        Node.__init__(self, (x, y))

    def is_neighbor(self, other):
        if self == other:
            return False
        if self.x == other.x and abs(self.y - other.y) == 1:
            return True
        if self.y == other.y and abs(self.x - other.x) == 1:
            return True
        return False
