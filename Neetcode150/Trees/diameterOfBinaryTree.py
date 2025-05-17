# https://leetcode.com/problems/diameter-of-binary-tree/description/
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def height(root):
            if not root:
                return 0
            return 1 + max(height(root.left), height(root.right))  # standard formula

        if not root:
            return 0
        # 3 options
        op1 = height(root.left) + height(root.right)
        # skewed tree options
        op2 = self.diameterOfBinaryTree(root.left)
        op3 = self.diameterOfBinaryTree(root.right)
        return max(op1, max(op2, op3))


# Solution 2
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0

        def height(root):
            nonlocal ans
            if not root:
                return 0
            left = height(root.left)
            right = height(root.right)
            ans = max(ans, left + right)  # no negative
            return 1 + max(left, right)  # including node

        height(root)
        return ans
