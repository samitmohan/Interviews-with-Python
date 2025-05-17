# https://leetcode.com/problems/count-good-nodes-in-binary-tree/
"""
Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.

Return the number of good nodes in the binary tree.

Use preorder : Node Left Right
Time and Space : O(n)
3 -> good node
  how many good nodes in left and right ST
  if left node val > node we passed through before (3) : not good node
    keep a max.
"""


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def preorder(
            root, max_value
        ):  # computes good node (for root and then recurisvely for others)
            if not root:
                return 0
            # non empty node
            ans = (
                1 if root.val >= max_value else 0
            )  # 1 => count of good node, 0 => not good node
            max_value = max(max_value, root.val)
            ans += preorder(root.left, max_value)  # counting number of nodes
            ans += preorder(root.right, max_value)
            return ans

        return preorder(root, root.val)  # root node will always be good node
