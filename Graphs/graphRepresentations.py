# Implementation of Graph using Adjacency Matrix

class GraphUsingAdjacencyMatrix:
    def __init__ (self, vertices, edges, rows, columns):
        self.vertices = vertices
        self.edges = edges
        self.rows = rows
        self.columns = columns
        adjacentMatrix = [[0 for i in range (vertices)] for j in range (vertices)]
        for k in range (vertices):
            adjacentMatrix[rows][columns] = 1
            adjacentMatrix[columns][rows] = 1


# Implementation of Graph using Adjacency List 
class AdjacentNode:
    def __init__ (self, data):
        self.vertex = data
        self.next = None

class Graph:
    def __init__ (self, vertices):
        self.V = vertices
        self.graph = [None] * self.V

    def insertEdge (self, source, destination):
        # Adds Node to Source Node 
        node = AdjacentNode (destination)
        node.next = self.graph[source]
        self.graph[source] = node
        # Adds Source Node to destination because this is undirected graph 
        node = AdjacentNode (source)
        node.next = self.graph[destination]
        self.graph[destination] = node

    # Print the graph 
    def displayGraph (self):
        for i in range (self.V):
            print (f'Adjacency List of Vertex {i} is given', end = " ")
            temp = self.graph[i]
            while temp:
                print (f'{temp.vertex}', end = " ")
                temp = temp.next
            print ('\n')


if __name__ == "__main__":
    graph = Graph(5)
    graph.insertEdge(0, 1)
    graph.insertEdge(0, 4)
    graph.insertEdge(1, 2)
    graph.insertEdge(1, 3)
    graph.insertEdge(1, 4)
    graph.insertEdge(2, 3)
    graph.insertEdge(3, 4)
    graph.displayGraph()