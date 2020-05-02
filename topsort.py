class TopSort:

    @staticmethod
    def kahns(graph):
        pass

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
