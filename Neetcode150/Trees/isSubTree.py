# https://leetcode.com/problems/subtree-of-another-tree/description/


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subroot: Optional[TreeNode]) -> bool:
        if not subroot:
            return True
        if not root:
            return False

        if self.sameTree(root, subroot):
            return True
        return self.isSubtree(root.left, subroot) or self.isSubtree(root.right, subroot)

    def sameTree(self, root, subroot):
        if not root and not subroot:
            return True
        if root and subroot and root.val == subroot.val:
            return self.sameTree(root.left, subroot.left) and self.sameTree(
                root.right, subroot.right
            )
        return False
