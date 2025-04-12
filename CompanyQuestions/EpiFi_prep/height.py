class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_height(root):
    if not root:
        return 0

    max_left = max_height(root.left) + 1  # height from the left side
    max_right = max_height(root.right) + 1  # height from the right side

    return max(max_left, max_right)
