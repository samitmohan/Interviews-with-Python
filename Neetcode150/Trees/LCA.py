# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


"""
if left_depth == right_depth:
    they are the same depth, return the curr node
if left_depth < right_depth:


if left: return left
if right: return right
return None

Time: O(N) — visits each node once
"""


class Solution:
    def lowestCommonAncestor(self, root, p, q):
        def dfs(root):
            if not root:
                return None
            if root == p or root == q:
                return root
            left = dfs(root.left)
            right = dfs(root.right)
            if left and right:
                # current node is LCA
                return root
            return left or right

        return dfs(root)
