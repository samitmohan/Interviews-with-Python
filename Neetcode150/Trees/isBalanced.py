class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(root):
            if not root:
                return 0
            return 1 + max(height(root.left), height(root.right))  # standard formula

        if not root:
            return True
        left = self.isBalanced(root.left)
        right = self.isBalanced(root.right)
        difference = abs(height(root.left) - height(root.right)) <= 1
        if left and right and difference:
            return True
        return False
