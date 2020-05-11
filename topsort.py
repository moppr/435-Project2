from collections import deque


class TopSort:

    @staticmethod
    def kahns(graph):
        all_nodes = graph.get_all_nodes()
        in_degrees = {node : 0 for node in all_nodes}
        for node in all_nodes:
            for other in node.edges:
                in_degrees[other] += 1

        output = []
        queue = deque()
        for node in in_degrees:
            if in_degrees[node] == 0:
                queue.append(node)

        while queue:
            node = queue[0]
            output.append(node)
            for other in node.edges:
                in_degrees[other] -= 1
            in_degrees[node] -= 1
            for other in node.edges:
                if in_degrees[other] == 0:
                    queue.append(other)
            queue.remove(node)

        return output

    @staticmethod
    def mdfs(graph):
        nodes = graph.get_all_nodes()
        stack = []
        visited = set()

        def dfs(node):
            visited.add(node)
            for other in node.edges:
                if other not in visited:
                    dfs(other)
            stack.append(node)

        for node in nodes:
            if node not in visited:
                dfs(node)

        return reversed(stack)
