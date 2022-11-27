# Implementation of BFS traversal :
# - Declare a queue and insert the starting vertex.
# - Initialize a visited array and mark the starting vertex as visited.
# - Follow the below process till the queue becomes empty:
#     - Remove the first vertex of the queue.
#     - Mark that vertex as visited.
#     - Insert all the unvisited neighbours of the vertex into the queue.

# Time Complexity: O(V+E), where V is the number of nodes and E is the number of edges.
# Auxiliary Space: O(V)

from collections import defaultdict

class Graph:
    def __init__ (self):
        self.graph = defaultdict (list)

    def addEdge (self, u, v):
        self.graph[u].append(v)
    
    def bfsTraversal (self, source):
        visited = [False] * (max (self.graph) + 1)
        queue = list ()
        queue.append (source)
        visited[source] = True

        while queue:
            source = queue.pop (0)
            print (source, end = " ")

            for i in self.graph[source]:
                if visited[i] == False:
                    queue.append (i)
                    visited[i] = True

if __name__ == '__main__':
    g = Graph ()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)
    
    print ("Following is Breadth First Traversal"
                    " (starting from vertex 2)")
    g.bfsTraversal(2)