# Using adjaceny list
"""
Adjacency List:
An Adjacency list is an array consisting of the address of all the linked lists.
The first node of the linked list represents the vertex and the remaining lists connected to this node represents the vertices to which this node is connected.
This representation can also be used to represent a weighted graph.
The linked list can slightly be changed to even store the weight of the edge.

Adjacency Matrix:
Adjacency Matrix is a 2D array of size V x V where V is the number of vertices in a graph.
Let the 2D array be adj[][], a slot adj[i][j] = 1 indicates that there is an edge from vertex i to vertex j.
Adjacency matrix for undirected graph is always symmetric.
Adjacency Matrix is also used to represent weighted graphs. If adj[i][j] = w, then there is an edge from vertex i to vertex j with weight w.
"""


class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []

    def add_edge(self, v1, v2):
        if v1 in self.adj_list and v2 in self.adj_list:
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)

    def remove_edge(self, v1, v2):
        if v1 in self.adj_list and v2 in self.adj_list:
            self.adj_list[v1].remove(v2)
            self.adj_list[v2].remove(v1)

    def remove_vertex(self, vertex):
        if vertex in self.adj_list:
            for v in self.adj_list[vertex]:
                self.adj_list[v].remove(vertex)
            del self.adj_list[vertex]


g = Graph()
g.add_vertex(1)
g.add_vertex(2)
g.add_vertex(3)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.remove_edge(1, 2)
g.remove_vertex(2)


# Using adjacency matrix


class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adj_matrix = [[0] * num_vertices for _ in range(num_vertices)]

    def add_edge(self, v1, v2):
        if v1 < self.num_vertices and v2 < self.num_vertices:
            self.adj_matrix[v1][v2] = 1
            self.adj_matrix[v2][v1] = 1

    def remove_edge(self, v1, v2):
        if v1 < self.num_vertices and v2 < self.num_vertices:
            self.adj_matrix[v1][v2] = 0
            self.adj_matrix[v2][v1] = 0

    # returns a string representation of the adjacency matrix.
    def __str__(self):
        return "\n".join([" ".join(map(str, row)) for row in self.adj_matrix])


g = Graph(3)
g.add_edge(0, 1)
g.add_edge(1, 2)
print(g)  # prints the adjacency matrix
g.remove_edge(0, 1)
print(g)  # prints the updated adjacency matrix

"""
Output
0 1 0
1 0 1
0 1 0
0 0 0
0 0 0
"""
