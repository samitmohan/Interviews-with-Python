# https://leetcode.com/problems/invert-binary-tree/


class Solution:
    def invertTree(self, root):
        if root:
            self.invertTree(root.left)
            self.invertTree(root.right)
            root.left, root.right = root.right, root.left
        return root
