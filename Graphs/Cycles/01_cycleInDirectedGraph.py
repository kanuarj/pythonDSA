# Finding the cycle in a directed graph done using DFS traversal.

from collections import defaultdict

class Graph:
    def __init__ (self, vertices):
        self.graph = defaultdict (list)
        self.V = vertices

    def addEdge (self, u, v):
        self.graph[u].append(v)

    def dfsCycle (self, vertex, visited, pathVisited):
        # Marks the current node as visited by default before execution
        visited[vertex] = True
        pathVisited[vertex] = True

        # Recursion for all neighbors is performed and if any neighbor is in stack then cycle is formed
        for neighbor in self.graph[vertex]:
            if visited[neighbor] == False:
                if self.dfsCycle (neighbor, visited, pathVisited) == True:
                    return True
            elif pathVisited[neighbor] == True:
                return True
        
        # Nodes from the stack need to be popped before function ends
        pathVisited[vertex] = False
        return False

    # Function returns True/False if there is a cycle formed
    def isCyclic (self):
        visited = [False] * (self.V + 1)
        pathVisited = [False] * (self.V + 1)

        for node in range (self.V):
            if visited[node] == False:
                if self.dfsCycle (node, visited, pathVisited) == True:
                    return True
        return False

if __name__ == '__main__':
    g = Graph (10)
    g.addEdge (1, 2)
    g.addEdge (2, 3)
    g.addEdge (3, 4)
    g.addEdge (4, 5)
    g.addEdge (5, 6)
    g.addEdge (3, 7)
    g.addEdge (8, 2)
    g.addEdge (8, 9)
    g.addEdge (9, 10)
    g.addEdge (10, 8)
    outcome = g.isCyclic ()
    print (outcome)