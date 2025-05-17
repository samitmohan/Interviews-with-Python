# https://leetcode.com/problems/binary-tree-maximum-path-sum/submissions/857939779/
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # find max in left and max in right
        # ignore all negative values and find left max
        # ignore all negative values and find right max
        # now you have left and right max for all nodes, generalise and return max
        self.maximum = float("-inf")

        def helper(root):
            if not root:
                return 0
            left = max(0, helper(root.left))
            right = max(0, helper(root.right))
            self.maximum = max(self.maximum, left + right + root.val)  # for that node

            # generalised answer
            return max(left, right) + root.val

        helper(root)
        return self.maximum
