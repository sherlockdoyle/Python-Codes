import random

class Graph:
    """
    Basic Graph class. Does not support parallel edges with same direction.
    Vertices must be 0 indexed. Indexing is allowed
    >>> g = Graph.complete()
    >>> g[0, 1]  # 1
    >>> g[1, 0] = 2

    :param int n: Create a graph with n edges.
    """
    def __init__(self, n):
        self.n = n
        self.adj_list = [{} for i in range(n)]

    def add_vert(self, n=1):
        """
        Add `n` vertices to the graph.
        """
        self.n += n
        self.adj_list.extend({} for i in range(n))

    def add_edge(self, frm, to, weight=1, order=0):
        """
        Add an edge to the graph starting between `frm` and `to` with `weight`
        weight.

        :param int order: Direction of the edge. 0 is bidirectional, 1 means
            from `frm` to `to`, -1 means from `to` to `frm`.
        """
        if order == 0:
            self.adj_list[a][b] = weight
            self.adj_list[b][a] = weight
        elif order < 0:
            self.adj_list[b][a] = weight
        else:
            self.adj_list[a][b] = weight

    def add_graph(self, g):
        """
        Add a new graph `g` as a seperate disconnected component.
        """
        n = self.n
        self.add_vert(g.n)
        for i, verts in enumerate(g.adj_list):
            for j, w in verts.items():
                self.adj_list[i + n][j + n] = w

    def shuffle(self):
        """
        Shuffle the vertex number of the graph.
        """
        perm = [i for i in range(self.n)]
        random.shuffle(perm)
        al = [{} for i in range(self.n)]
        for i, verts in enumerate(self.adj_list):
            for j, w in verts.items():
                al[perm[i]][perm[j]] = self.adj_list[i][j]
        self.adj_list = al

    def randomize_weights(self, low=-5, high=15):
        """
        Add random weights between low and high to all the edges.
        """
        for i, verts in enumerate(self.adj_list):
            for j in verts:
                self.adj_list[i][j] = random.randint(low, high)

    def num_edges(self):
        """
        Returns the total number of edges. bidirectional edges are counted
        twice.
        """
        return sum(len(verts) for verts in self.adj_list)

    def get_edges(self, half=False):
        """
        Returns an edge iterator. Each element is (from, to, weight). If `half`
        is True, bidirectional edges are returned only once such that from <=
        to.
        """
        for i, verts in enumerate(self.adj_list):
            for j, w in verts.items():
                if half:
                    if i <= j:
                        yield i, j, w
                else:
                    yield i, j, w
    
    def get_adj_mat(self, def_weight=0):
        """
        Returns the adjacency matrix representation of the graph.

        :param int def_weight: Default weight to use for non-existent edges.
        """
        mat = [[def_weight] * self.n for _ in range(self.n)]
        for i, verts in enumerate(self.adj_list):
            for v, w in verts.items():
                mat[i][v] = w
        return mat
    
    def __str__(self):
        s = ""
        for i, verts in enumerate(self.adj_list):
            s += f'{i}:'
            for j, w in verts.items():
                s += f' ({j}: {w}),'
            s = s[:-1] + '\n'
        return s
    
    def __getitem__(self, idx):
        if isinstance(idx, tuple):
            return self.adj_list[idx[0]][idx[1]]\
                if idx[1] in self.adj_list[idx[0]] else None
        return self.adj_list[idx]
    
    def __setitem__(self, idx, val):
        if isinstance(idx, tuple):
            if idx[0]<0 or idx[0]>=self.n or idx[1]<0 or idx[1]>=self.n:
                raise IndexError(f'Index must be within 0 to {self.n}.')
            self.adj_list[idx[0]][idx[1]] = val
        else:
            raise TypeError('Index must be a 2-uple.')
    
    def visualize(self):
        """
        Returns a graphviz.Digraph object for visualization.
        """
        from graphviz import Digraph
        g = Digraph()
        for i, verts in enumerate(self.adj_list):
            for j, w in verts.items():
                g.edge(str(i), str(j), str(w))
        return g
    
    @staticmethod
    def from_adj_mat(mat, def_weight=0):
        """
        Builds a graph from the adjacency matrix `mat`. Entry with `def_weight`
        represent non-existent edges.
        """
        if len(mat) != len(mat[0]):
            raise IndexError('Non squre adjacency matrix.')
        g = Graph(len(mat))
        for i, row in enumerate(mat):
            for j, w in enumerate(row):
                if w != def_weight:
                    g.adj_list[i][j] = w
        return g

    @staticmethod
    def from_edges(edges):
        """
        Builds a graph from a list of edges as (from, to, weight). If absent,
        weight is set to 1. All edges must be 0-indexed integers.
        """
        edges = list(edges)
        g = Graph(max(max(e[0], e[1]) for e in edges) + 1)
        for e in edges:
            g.adj_list[e[0]][e[1]] = e[2]
        return g

    @staticmethod
    def complete(k=5):
        """
        Returns a complete graph with `k` vertices.
        """
        g = Graph(k)
        for i in range(k):
            for j in range(i + 1, k):
                g.adj_list[i][j] = g.adj_list[j][i] = 1
        return g

    @staticmethod
    def cycle(k=5):
        """
        Returns a cycle  with `k` vertices.
        """
        g = Graph(k)
        for i in range(k):
            g.adj_list[i][(i + 1) % k] = g.adj_list[(i + 1) % k][i] = 1
        return g

    @staticmethod
    def wheel(k=5):
        """
        Returns a wheel with `k` + 1 vertices.
        """
        g = Graph(k + 1)
        for i in range(k):
            g.adj_list[i][(i + 1) % k] = g.adj_list[(i + 1) % k][i] = 1
            g.adj_list[k][i] = g.adj_list[i][k] = 1
        return g

    @staticmethod
    def cube(n=3):
        """
        Returns a `n` dimensional hypercube graph.
        """
        g = Graph(2 ** n)
        for i in range(2 ** n):
            for j in range(n):
                g.adj_list[i][i ^ (1 << j)] = 1
        return g

    @staticmethod
    def bipartite(a=2, b=3):
        """
        Returns a bipartite graph with `a` and `b` vertices in the two
        partitions.
        """
        g = Graph(a + b)
        for i in range(a):
            for j in range(b):
                g.adj_list[i][j + a] = g.adj_list[j + a][i] = 1
        return g