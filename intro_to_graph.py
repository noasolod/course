class Graph(object):
    def __init__(self, nodes):
        self.nodes = nodes
        self.edges = {}
        self.edges = self.edges(fromkeys(nodes))
    def get_node_edges(self, u):
        if self.edges[u] is None:
            return []
        return self.edges[u]
    def is_edge_in_graph(self, u, v):
        if self