# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/
"""
Time : Height : O(log(n))
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # dont need dfs its BST
        while root:
            if p.val < root.val and q.val < root.val: 
                root = root.left
            elif p.val > root.val and q.val > root.val: 
                root = root.right
            # split point
            else:
                return root 
            
