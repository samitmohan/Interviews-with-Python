# // https: // leetcode.com / problems / range - sum - of - bst


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root, low, high):
        # just check if low <= val <= high -> if yes then add in sum var
        # recursive calls to left and right
        # if no root then just return

        if not root:
            return 0

        if root.val < low:
            return self.rangeSumBST(root.right, low, high)  # look in right
        elif root.val > high:
            return self.rangeSumBST(root.left, low, high)  # look in left

        # else answer found
        return (
            root.val
            + self.rangeSumBST(root.left, low, high)
            + self.rangeSumBST(root.right, low, high)
        )
