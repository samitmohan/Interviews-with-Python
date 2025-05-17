# https://leetcode.com/problems/merge-two-binary-trees/description/


class Solution:
    def mergeTrees(
        self, t1: Optional[TreeNode], t2: Optional[TreeNode]
    ) -> Optional[TreeNode]:
        # base case
        if not t1 and not t2:
            return None
        v1 = t1.val if t1 else 0
        v2 = t2.val if t2 else 0
        root = TreeNode(v1 + v2)
        root.left = self.mergeTrees(t1.left if t1 else None, t2.left if t2 else None)
        root.right = self.mergeTrees(t1.right if t1 else None, t2.right if t2 else None)
        return root
