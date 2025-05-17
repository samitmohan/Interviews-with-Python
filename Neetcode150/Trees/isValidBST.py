# https://leetcode.com/problems/validate-binary-search-tree/description/
# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.

# Inorder : Left Root Right : do inorder traversal if it's in sorted order -> BST.


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        arr = []

        def inorder(root):
            if root is None:
                return None
            inorder(root.left)
            arr.append(root.val)
            inorder(root.right)

        inorder(root)
        # check if it's sorted
        for i in range(1, len(arr)):
            if arr[i] <= arr[i - 1]:
                return False
        return True
