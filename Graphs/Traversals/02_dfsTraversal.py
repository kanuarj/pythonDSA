# Time complexity: O(V + E), where V is the number of vertices and E is the number of edges in the graph.
# Auxiliary Space: O(V), since an extra visited array of size V is required.

from collections import defaultdict

class Graph:
    def __init__ (self):
        self.graph = defaultdict (list)

    def addEdge (self, u, v):
        self.graph[u].append (v)

    def dfsConnectedGraph (self, vertex):
        visited = set ()
        self.dfsFunction (vertex, visited)

    def dfsDisconnectedGraph (self):
        visited = set ()
        for vertex in self.graph:
            if vertex not in visited:
                self.dfsFunction (vertex, visited)

    def dfsFunction (self, vertex, visited):
        visited.add (vertex)
        print (vertex, end = ' ')
        for neighbor in self.graph[vertex]:
            if neighbor not in visited:
                self.dfsFunction (neighbor, visited)

if __name__ == '__main__':
    g = Graph ()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)
    g.dfsDisconnectedGraph ()