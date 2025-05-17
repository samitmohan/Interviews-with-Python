# https://leetcode.com/problems/minimum-distance-between-bst-nodes/description/
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        # Solution : Sort elements (in-order traversal in BST) : [1, 2, 3, 4, 6]
        # Compute difference of adjacent nodes and find min. [1-2 : 1, 2-3 : 1, 3-4 : 1, 4-6 : 2] : min([1,1,1,2]) = 1
        # Keep track of prev node, initially : NULL, once we go to 2, prev = 1 and just find min(node.val - prev.val)
        prev, ans = None, float("inf")

        def inorder(node):
            if not node:
                return
            inorder(node.left)
            nonlocal prev, ans  # in python : not global variables hence need to declare here
            # process root
            if prev:
                ans = min(ans, node.val - prev.val)
            prev = node
            inorder(node.right)

        inorder(root)
        return ans
