# https://leetcode.com/problems/find-mode-in-binary-search-tree/?envType=daily-question&envId=2023-11-01


class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        self.ans = []

        def inorder(root):
            if not root:
                return
            self.ans.append(root.val)
            inorder(root.left)
            inorder(root.right)
