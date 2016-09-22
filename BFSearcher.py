

class BFPathFinder():
    def __init__(self, graph, vertex):
        self.graph = graph
        self.vertex = vertex
        self.edge_to = {}
        self.dist_to = {}
        self.marked = set([])
        self._bfs(self.vertex)

    def _bfs(self, vertex):


    def distance(self, vertex):
        return self.dist_to.get(vertex)

    def path_to(self, vertex):

    def has_path_to(self, vertex):
        return vertex in self.marked
