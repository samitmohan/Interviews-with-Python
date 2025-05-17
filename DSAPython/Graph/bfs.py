from collections import deque


# How to use in LC questions
class Solution:
    def dfs(root):
        queue = deque()
        queue.append(root)
        while queue:
            curr = queue.popleft()
            print(curr.val)
            if curr.right:
                queue.append(curr.right)
            if curr.left:
                queue.append(curr.left)


def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)

    while queue:
        vertex = queue.popleft()
        print(vertex)

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)


graph = {
    "A": ["C", "E"],
    "B": [],
    "C": ["B", "G"],
    "D": [],
    "E": ["H"],
    "H": ["D"],
    "G": [],
}
bfs(graph, "A")
# you should get ['A','C','E','B','G','H','D']

graph2 = {0: [1, 2], 1: [2], 2: [0, 3], 3: [3]}

bfs(graph2, 2)
