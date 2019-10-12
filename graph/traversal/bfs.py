from Graph import Graph
from collections import deque

def bfs(self, start=0):
    """
    Does a bredth first traversal starting from vertex `start`. Returns the
    order of the traversal, BFS parent of each vertex, level of each vertex in
    BFS tree.
    """
    visited = [False] * self.n
    queue = deque([start])
    order, parent, level = [start], [None] * self.n, [0] * self.n
    visited[start] = True
    while len(queue) > 0:
        v = queue.popleft()
        for i in self.adj_list[v]:
            if not visited[i]:
                queue.append(i)
                order.append(i)
                visited[i] = True
                parent[i] = v
                level[i] = level[v] + 1
    return order, parent, level
Graph.bfs = bfs


def main():
    g = Graph.bipartite(1, 1)
    g.add_graph(Graph.bipartite(2, 1))
    g.add_graph(Graph.bipartite(2, 2))
    g.add_graph(Graph.bipartite(2, 3))
    g.add_graph(Graph.bipartite(1, 2))
    g.add_edge(0, 2)
    g.add_edge(1, 5)
    g.add_edge(2, 9)
    g.add_edge(3, 14)
    print('Graph', '_____', g, sep='\n')
    o, p, l = g.bfs(0)
    print('Bredth first traversel starting from vertex 0:', *o)
    print('Parent of each vertex:', *p)
    print('Level of each vertex:', *l)