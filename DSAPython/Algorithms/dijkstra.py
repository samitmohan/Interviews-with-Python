from heapq import heappush, heappop
from collections import defaultdict

# Find shortest path from start node to all other nodes with non negative weights.

def dijkstra(graph, start):
    dist = defaultdict(lambda: float('inf'))
    dist[start] = 0
    vis = set() # to keep track of visited nodes
    heap = []
    heappush(heap, (0, start)) # push 0, 'A' -> distance to A is 0 from 0

    #Go through all neighbors of currNode.
    while heap:
        distance, currNode = heappop(heap)
        if currNode in vis: continue
        vis.add(currNode) # Pick the node with the smallest tentative distance, mark it.
        # neighbour check
        for neighbor, wt in graph[currNode].items():
            if neighbor in vis: continue
            newDist = distance + wt # distance from the start node to that neighbor via currNode.
            if newDist < dist[neighbor]:
                dist[neighbor] = newDist
                heappush(heap, (newDist, neighbor)) # 1,B or 4, C
    return dist

'''
Better with class
'''

class Graph:
    def __init__(self, graph: dict = {}):
        self.graph = graph

    def add_edge(self, node1, node2, weight):
        if node1 not in self.graph:
            self.graph[node1] = {}
        self.graph[node1][node2] = weight

    def shortest_distances(self, source: str):
        dist = defaultdict(lambda: float('inf'))
        dist[source] = 0
        vis = set()
        heap = [(0, source)]

        while heap:
            distance, currNode = heappop(heap)
            if currNode in vis:
                continue
            vis.add(currNode)
            for neighbor, wt in self.graph.get(currNode, {}).items():
                if neighbor in vis:
                    continue
                newDist = distance + wt
                if newDist < dist[neighbor]:
                    dist[neighbor] = newDist
                    heappush(heap, (newDist, neighbor))
        return dist

graph = {
    "A": {"B": 3, "C": 3},
    "B": {"A": 3, "D": 3.5, "E": 2.8},
    "C": {"A": 3, "E": 2.8, "F": 3.5},
    "D": {"B": 3.5, "E": 3.1, "G": 10},
    "E": {"B": 2.8, "C": 2.8, "D": 3.1, "G": 7},
    "F": {"G": 2.5, "C": 3.5},
    "G": {"F": 2.5, "E": 7, "D": 10},
}

G = Graph(graph)

# Run the shortest path from node B
distances = G.shortest_distances("B")
to_F = distances["F"]
print(f"The shortest distance from B to F is {to_F}")
