class Node:
    def __init__(self, val=0, neighbors=[]):
        self.val = val
        self.neighbors = neighbors


"""
Deep Copy : new graph with same structure and same values

Hashmap and DFS.
HashMap (old : new)
    1-2
    | |
    3-4
Start at 1, create copy of 1. (original has 2 neighbours)
For 2 and 3 nodes -> need to create copy.

1 : 1 (old : new)

node 2. 1 -> 2
2 : 2 (old : new)
2 has two neighbours, 1 and 4
Try to create 1 but 1 already present in hashmap so add 2->1 edge (undirected : both ways)
Create node 4
4 : 4 (old : new)

So on... DFS.

Time : O(n) where n = E + V
"""


# map old nodes -> new nodes


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        old_to_new = {}

        def dfs(node):
            if node in old_to_new:
                return old_to_new[node]  # just return
            copy = Node(node.val)
            old_to_new[node] = copy

            # recursive for all
            for neighbor in node.neighbors:
                copy.neighbors.append(dfs(neighbor))  # returns copy of node
            return copy

        return dfs(node) if node else None
