"""
To implement DFS, we use the Stack data structure to keep track of the visited nodes. We begin with the root as the first element in the stack, then pop from it and add all the related nodes of the popped node to the stack. We repeated the process until the stack became empty.

Every time we reach a new node, we will take the following steps:

We add the node to the top of the stack.
Marked it as visited.
We check if this node has any adjacent nodes:
If it has adjacent nodes, then we ensure that they have not been visited already, and then visited it.
We removed it from the stack if it had no adjacent nodes.
With every node added to the stack, we repeat the above steps or recursively visit each node until we reach the dead end.
"""


# How to use in LC questions
class Solution:
    def dfs(root):
        stack = [root]
        while stack:
            curr = stack.pop()
            print(curr.val)
            if curr.right:
                stack.append(curr.right)
            if curr.left:
                stack.append(curr.left)


# General DFS


def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start)

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)


graph = {"A": ["B", "C"], "B": ["D", "E"], "C": ["F"], "D": [], "E": ["F"], "F": []}
dfs(graph, "A")
# this will return the sequence of A,B,D,E,F,C

graph2 = {0: [1, 2], 1: [2], 2: [0, 3], 3: [3]}
dfs(graph2, 2)  # 2 0 1 3
