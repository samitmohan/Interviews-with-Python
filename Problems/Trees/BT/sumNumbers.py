# https://leetcode.com/problems/sum-root-to-leaf-numbers://leetcode.com/problems/sum-root-to-leaf-numbers/
# Answer : currSum = currSum * 10 + root.val (1->2 : 1 * 10 + 2 = 12) [do for left ST and right ST and add]


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def sumRecursive(root, currSum):
            if not root:
                return 0
            currSum = currSum * 10 + root.val
            # base case
            if not root.left and not root.right:
                return currSum
            # recursive case
            left_sum = sumRecursive(root.left, currSum)
            right_sum = sumRecursive(root.right, currSum)
            ans = left_sum + right_sum
            return ans

        return sumRecursive(root, 0)
