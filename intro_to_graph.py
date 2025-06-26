class Graph(object):
    def __init__(self, nodes):
        self.nodes = nodes
        keys = nodes
        vals = [list() for i in range(len(nodes))]
        self.edges = dict(zip(keys, vals))
    def __str__(self):
        return f"{self.nodes}, {self.edges}"
    def get_nodes(self):
        return self.nodes
    def get_edges(self):
        return self.edges
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

def dfs_rec(g: Graph, act_on: int, marked: list[bool], visited: list, i_of_act_on: int):
    current_neighbours = g.get_node_edges(act_on)
    for edge in current_neighbours:
        if not marked[edge]:
            marked[edge] = True
            visited.append(edge)
            return dfs_rec(g, edge, marked, visited, i_of_act_on)
    if act_on == visited[0]:
        return visited
    i_of_act_on -= 1
    return dfs_rec(g, visited[i_of_act_on], marked, visited, i_of_act_on)

def dfs(graph: Graph, u: int):
    marked = [False] * len(graph.get_nodes())
    marked[u] = True
    visited = [u]
    return dfs_rec(graph, u, marked, visited, -1)

my_g = Graph([0,1,2,3,4,5,6,7,8,9])
my_g.add_edge_to_graph(0, 8)
my_g.add_edge_to_graph(0, 1)
my_g.add_edge_to_graph(0, 7)
my_g.add_edge_to_graph(1, 4)
my_g.add_edge_to_graph(2, 6)
my_g.add_edge_to_graph(3, 5)
my_g.add_edge_to_graph(3, 6)
my_g.add_edge_to_graph(4, 9)
my_g.add_edge_to_graph(4, 0)
my_g.add_edge_to_graph(4, 3)
my_g.add_edge_to_graph(4, 5)
my_g.add_edge_to_graph(6, 2)
my_g.add_edge_to_graph(6, 5)
my_g.add_edge_to_graph(7, 2)
my_g.add_edge_to_graph(7, 3)
my_g.add_edge_to_graph(7, 8)
my_g.add_edge_to_graph(8, 7)
my_g.add_edge_to_graph(8, 1)
my_g.add_edge_to_graph(8, 0)
my_g.add_edge_to_graph(9, 0)
print(my_g)

print(dfs(my_g, 4))