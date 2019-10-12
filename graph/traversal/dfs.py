from Graph import Graph
from collections import deque

def dfs(self, start=0):
    """
    Non recursive depth first traversal starting from vertex `start`.
    """
    visited = [False] * self.n
    stack = deque([start])
    order = []
    while len(stack) > 0:
        v = stack.pop()
        if not visited[v]:
            visited[v] = True
            order.append(v)
        for i in self.adj_list[v]:
            if not visited[i]:
                stack.append(i)
    return order
Graph.dfs = dfs

def dfs_recursive(self, start=0):
    """
    Recursive depth first traversal starting from vertex `start`.
    """
    visited = [False] * self.n
    order = [start]
    visited[start] = True

    def dfs_util(v):
        for i in self.adj_list[v]:
            if not visited[i]:
                order.append(i)
                visited[i] = True
                dfs_util(i)
    
    dfs_util(start)
    return order
Graph.dfs_recursive = dfs_recursive

def components(self):
    """
    Returns a list containing the number of the components of each of the
    vertices.
    """
    visited = [False] * self.n
    comps = [0] * self.n
    comp = 0

    def dfs_util(v):
        for i in self.adj_list[v]:
            if not visited[i]:
                comps[i] = comp
                visited[i] = True
                dfs_util(i)

    for i in range(self.n):
        if not visited[i]:
            comp += 1
            dfs_util(i)
    return comps
Graph.components = components


def main():
    g = Graph.bipartite(4, 5)
    print('Graph', '_____', g, sep='\n')
    print('Depth first traversel starting from vertex 0:', *g.dfs(0))
    print('Recursive depth first traversel:', *g.dfs_recursive(0))
    print('-' * 80)

    g2 = Graph.bipartite(1, 1)
    g2.add_graph(Graph.bipartite(1, 2))
    g2.add_graph(Graph.bipartite(2, 1))
    g2.shuffle()
    print('Graph', '_____', g2, sep='\n')
    print('Components:', *g2.components())