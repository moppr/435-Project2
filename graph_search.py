from collections import deque


class GraphSearch:
    """Recursive and iterative implementations of Depth first and Breadth first searches."""

    # "visited" for the following four methods implemented as a list and not a set
    # to preserve order and allow manual tracing of each method.
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
        all_nodes = graph.get_all_nodes()
        start = all_nodes.pop()
        queue = deque()
        queue.append(start)
        visited = [start]

        def bft_rec_helper(queue, visited):
            if not queue:
                return visited

            node = queue.popleft()

            for other in node.edges:
                if other not in visited:
                    all_nodes.remove(other)
                    queue.append(other)
                    visited.append(other)

            # Disconnect in the graph (queue empty but unvisited nodes exist).
            if all_nodes and not queue:
                next = all_nodes.pop()
                queue.append(next)
                visited.append(next)

            return bft_rec_helper(queue, visited)

        return bft_rec_helper(queue, visited)

    @staticmethod
    def bft_iter(graph):
        all_nodes = graph.get_all_nodes()
        start = all_nodes.pop()
        queue = deque()
        queue.append(start)
        visited = [start]

        while queue:
            node = queue.popleft()
            for other in node.edges:
                if other not in visited:
                    all_nodes.remove(other)
                    queue.append(other)
                    visited.append(other)

            # Disconnect in the graph (queue empty but unvisited nodes exist).
            if all_nodes and not queue:
                next = all_nodes.pop()
                queue.append(next)
                visited.append(next)

        return visited

    @staticmethod
    def cut_cycles(graph):
        # TODO: Implement iteratively
        nodes = graph.get_all_nodes()
        visited = set()
        checked = set()

        def cut_cycles(node):
            visited.add(node)
            for other in node.edges.copy():
                if other in checked:
                    continue
                elif other in visited:
                    graph.remove_directed_edge(node, other)
                else:
                    cut_cycles(other)
            visited.remove(node)
            checked.add(node)

        while nodes:
            cut_cycles(nodes.pop())
            nodes -= checked

        GraphSearch._verify_no_cycles(graph)

        return graph

    @staticmethod
    def _verify_no_cycles(graph):
        # TODO: Implement iteratively
        nodes = graph.get_all_nodes()
        visited = set()

        def is_cyclic(node):
            if node in visited:
                return True
            visited.add(node)
            for other in node.edges:
                if is_cyclic(other):
                    return True
            visited.remove(node)

        for node in nodes:
            if is_cyclic(node):
                raise RuntimeError(f"Graph was still not cyclic after cycle removal\n{graph}")
