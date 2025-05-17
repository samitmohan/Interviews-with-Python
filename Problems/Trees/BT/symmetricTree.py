# https://leetcode.com/problems/symmetric-tree/
# Preorder for left tree, reverse preorder for right tree, compare.
class Solution:
    def isSymmetric(self, root):
        def preorder(st1, st2):
            # edge case
            if st1 is None and st2 is None:
                return True
            if st1 is None or st2 is None:
                return False

            return (
                st1.val == st2.val
                and preorder(st1.left, st2.right)
                and preorder(st1.right, st2.left)
            )

        return preorder(root.left, root.right)
