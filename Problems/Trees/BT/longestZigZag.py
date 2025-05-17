# https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/
# DFS


class Solution:
    def longestZigZag(self, root):
        return max(
            self.trversal(root.left, 0, False), self.trversal(root.right, 0, True)
        )

    def trversal(self, root, length, goleft):
        if not root:
            return length
        length += 1
        # goleft means should we should go left
        if goleft:
            leftlength = self.trversal(root.left, length, not goleft)
            rightlength = max(self.trversal(root.right, 0, goleft), length)
        else:
            leftlength = max(self.trversal(root.left, 0, goleft), length)
            rightlength = self.trversal(root.right, length, not goleft)
        return max(leftlength, rightlength)
