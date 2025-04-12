# https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/description/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Intuition, we want to find the kth distance node from the target node
# however, it is not easy to do this in a directed tree or graph,
# as a result, we should transfer the tree to a undirected graph

# Algo:
# step 1: Make a undirected graph
# step 2: Using BFS and iterate kth time, on each iteration,
#         it will give us the level-i value from target


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        # make a undirected graph
        graph = collections.defaultdict(list)

        def connect(parent, child):
            if parent and child:
                graph[parent.val].append(child.val)
                graph[child.val].append(parent.val)
            if child.left:
                connect(child, child.left)
            if child.right:
                connect(child, child.right)

        # initialize the graph, now the the binary search tree has been transfer to a undirected graph
        connect(None, root)

        visited = set()  # record the visited val, we do need to visit again
        ans = [target.val]  # record the ans, initialize as the target value
        # initialize the visited, we are right now at the target val
        visited.add(target.val)
        # begin to iterate throgh the level
        for level in range(k):
            curr_level = []  # record the val at the current level
            for parent in ans:
                for connected in graph[parent]:
                    if connected not in visited:
                        visited.add(connected)
                        curr_level.append(connected)
            ans = curr_level  # after one level, we should replace the prev level as the current level

        return ans
