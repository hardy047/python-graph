




class UnDirectedGraph():
    def __init__(self, vertex):
        self.graph = {}
        for v in vertex:
            self.graph[v] = set([])

    def add_vertex(self, vertex):
        self.graph[vertex] = set([])

    def add_edge(self, vertex_from, vertex_to):
        self.graph[vertex_from].add(vertex_to)
        self.graph[vertex_to].add(vertex_from)

    def get_all_vertex(self):
        return [v for v in self.graph.keys()]

    def get_adjacent_vertexes(self, vertex):
        return [v for v in self.graph[vertex]]


