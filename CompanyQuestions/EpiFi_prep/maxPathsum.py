# possible that negative values can be included : [2,-1,3]
class Solution:
    def maxPathSum(root):
        maximum = float('-inf')

        def helper(root):
            if not root:
                return 0
            left = max(0, helper(root.left))
            right = max(0, helper(root.right))
            maximum = max(maximum, left + right + root.val)  # for that node (this is for result)

            return max(left, right) + root.val  # max it can have : don't split

        helper(root)
        return maximum
