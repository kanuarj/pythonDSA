# Time Complexity: O(V+E). The above algorithm is simply DFS with an extra stack. So time complexity is the same as DFS
# Auxiliary space: O(V). The extra space is needed for the stack

# Algorithm :
# - Create a stack to store the nodes.
# - Initialize visited array of size N to keep the record of visited nodes.
# - Run a loop from 0 till N
#     - if the node is not marked True in visited array
#         - Call the recursive function for topological sort and perform the following steps.
#             - Mark the current node as True in the visited array.
#             - Run a loop on all the nodes which has a directed edge to the current node
#                 - if the node is not marked True in the visited array:
#                     - Recursively call the topological sort function on the node
#             - Push the current node in the stack.
# - Print all the elements in the stack.

from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict (list)
        self.V = vertices

    def addEdge (self, u, v):
        self.graph[u].append (v)

    def topologicalSort (self):
        visited = [False] * self.V
        stack = list ()

        for i in range (self.V):
            if visited[i] == False:
                self.dfsFunction (i, visited, stack)

        return stack[::-1]

    def dfsFunction (self, vertex, visited, stack):
        visited[vertex] = True

        for i in self.graph[vertex]:
            if visited[i] == False:
                self.dfsFunction (i, visited, stack)

        stack.append (vertex)

if __name__ == '__main__':
    g = Graph (6)
    g.addEdge (5, 0)
    g.addEdge (5, 2)
    g.addEdge (2, 3)
    g.addEdge (3, 1)
    g.addEdge (4, 0)
    g.addEdge (4, 1)
    outcome = g.topologicalSort ()
    print (f'The topological sort for given DAG is {outcome}')