from collections import deque


class GraphSearch:
    """Recursive and iterative implementations of Depth first and Breadth first searches."""

    @staticmethod
    def dfs_rec(start, end, visited=None):
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
        stack = [start]
        visited = []

        while stack:
            node = stack.pop()
            if node not in visited:
                visited.append(node)
            if node == end:
                return visited
            # Reversing causes the stack to behave identically to the recursive implementation.
            for other in reversed(list(node.edges)):
                if other not in visited:
                    stack.append(other)

    @staticmethod
    def bft_rec(graph):
        # TODO: account for graph not being connected, double check algorithm
        all_nodes = graph.get_all_nodes()
        start = all_nodes.pop()
        queue = deque()
        queue.append(start)

        def bft_rec_helper(queue, visited):
            if not queue:
                return visited

            node = queue.popleft()

            for other in node.edges:
                if other not in visited:
                    queue.append(other)
                    visited.append(other)

            return bft_rec_helper(queue, visited)

        return bft_rec_helper(queue, [start])
