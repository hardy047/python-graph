
class DFSearcher():
    def __init__(self, graph, vertex):
        self.graph = graph
        self.vertex = vertex
        self.marked = set([])
        self._dfs(self.vertex)

    def _dfs(self, vertex):
        self.marked.add(vertex)

        for v in self.graph.get_adjacent_vertexes(vertex):
            self._dfs(v) if v not in self.marked else continue

    def is_connected(self, vertex):
        return True if vertex in self.marked else False

    def get_all_connected(self):
        return self.marked

    def get_connected_count(self):
        return len(self.marked)
