class Graph(object):
    def __init__(self, nodes):
        self.nodes = nodes
        keys = nodes
        vals = [list() for i in range(len(nodes))]
        self.edges = dict(zip(keys, vals))
    def __str__(self):
        return f"{self.nodes}, {self.edges}"
    def get_node_edges(self, u):
        return self.edges[u]
    def is_edge_in_graph(self, u: int, v: int) -> bool:
        """
        :param u: a node in self
        :param v: a node in self
        :return: True if there is an edge connecting u and v. False otherwise.
        """
        if v in self.edges[u] or u in self.edges[v]:
            return True
        return False
    def add_edge_to_graph(self, u, v):
        """
        :param u: a node in self
        :param v: a node in self
        adds edge u -> v to node u
        :return: None
        """
        if v not in self.edges[u]:
            self.edges[u].append(v)

def exists_path_rec(g: Graph, v: int, r: list[int], i:list[list[int]]):
    if len(r) == 0:
        return False
    current_nodes = g.get_node_edges(r[-1])
    current_index = i[-1][-1]
    if current_index >= len(current_nodes) or current_nodes[current_index] in r:
        del r[-1]
        del i[-1]
        if len(i) > 0:
            i[-1].append((i[-1][-1]) + 1)
        return exists_path_rec(g, v, r, i)
    if current_nodes[current_index] == v or r[-1] == v:
        return True
    r.append(current_nodes[current_index])
    i.append([0])
    return exists_path_rec(g, v, r, i)

def exists_path_rec_n(g: Graph, v: int, r: list[int], i:list[list[int]], n: int):
    if len(r) == 0:
        return False
    current_nodes = g.get_node_edges(r[-1])
    current_index = i[-1][-1]
    if current_index >= len(current_nodes) or len(r) > n or current_nodes[current_index] in r:
        del r[-1]
        del i[-1]
        if len(i) > 0:
            i[-1].append((i[-1][-1]) + 1)
        return exists_path_rec(g, v, r, i)
    if current_nodes[current_index] == v:
            return True
    r.append(current_nodes[current_index])
    i.append([0])
    return exists_path_rec(g, v, r, i)

def exists_path_up_to_n(graph: Graph, u: int, v: int, n: int):
    """
    :param graph: Graph object
    :param u: int. a node in graph
    :param v: int. a node in graph
    :param n: int. max len of route
    :return: True if exist in graph a route from u to v with max len is n. False otherwise
    """
    if u == v:
        return True
    return exists_path_rec_n(graph, v, [u], [[0]], n)

def exists_path(graph: Graph, u: int, v: int):
    """
    :param graph: Graph object
    :param u: int. a node in graph
    :param v: int. a node in graph
    :return: True if exist in graph a route from u to v, False otherwise.
    """
    return exists_path_rec(graph, v, [u], [[0]])

my_g = Graph([0,1,2,3,4])
my_g.add_edge_to_graph(0, 2)
my_g.add_edge_to_graph(0, 4)
my_g.add_edge_to_graph(1, 4)
my_g.add_edge_to_graph(1, 3)
my_g.add_edge_to_graph(4, 1)
my_g.add_edge_to_graph(2, 4)
my_g.add_edge_to_graph(2, 3)
print(my_g)

print(exists_path(my_g, 2, 3))