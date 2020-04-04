class GraphSearch:
    """Recursive and iterative implementations of Depth first and Breadth first searches."""

    @staticmethod
    def dfs_rec(start, end, visited=None):
        """Return a depth-first search path implemented recursively"""
        if not visited:
            visited = []

        if start not in visited:
            visited.append(start)
            if start == end:
                return True
            for other in start.edges:
                if GraphSearch.dfs_rec(other, end, visited):
                    return visited

    @staticmethod
    def dfs_iter(start, end):
        """Return a depth-first search path implemented iteratively"""
        stack = [start]
        visited = []

        while stack:
            node = stack.pop()
            if node not in visited:
                visited.append(node)
            if node == end:
                return visited
            # reversing causes the stack to behave identically to the recursive implementation
            for other in reversed(list(node.edges)):
                if other not in visited:
                    stack.append(other)

    @staticmethod
    def bft_rec(graph):

        # TODO: account for graph not being connected, double check algorithm

        def bft_rec_helper(queue, visited):
            if not queue:
                return visited
            node = queue.pop()

            for other in node.edges:
                if other not in visited:
                    queue.append(other)
                    visited.append(other)

            return bft_rec_helper(queue, visited)

        # arbitrary starting point
        start = graph.get_node(0)

        return bft_rec_helper([start], [start])
