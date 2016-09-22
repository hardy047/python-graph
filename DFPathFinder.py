

class DFPathFinder():
    def __init__(self, graph, vertex):
        self.graph = graph
        self.vertex = vertex
        self.marked = set([])
        self.edge_to = {}

    def _dfs(self, vertex):
        self.marked.add(vertex)

        for v in self.graph.get_adjacent_vertexes(vertex):
            self.edge_to[v] = vertex
            self._dfs(v) if v not in self.marked else continue

    def has_path_to(self, vertex):
        return vertex in self.marked

    def path_to(self, vertex):
        if not self.has_path_to(vertex):
            return None

        while vertex:
            yield vertex
            vertex = self.edge_to.get(vertex)



