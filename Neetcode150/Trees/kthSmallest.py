# https://leetcode.com/problems/kth-smallest-element-in-a-bst/
# O(n) space and time : to improve use morris traversal
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans = []

        def inorder(root):
            if not root:
                return
            inorder(root.left)
            ans.append(root.val)
            inorder(root.right)

        inorder(root)
        return ans[k - 1]


# Optimised:

"""
Property oF BST : inorder : sorted
after inorder get the 3rd element
T & S : O(n) and O(n)

How to reduce space? Use a counter in the function. Once node reached in inorder : do counter += 1
  if counter == k (we have reached our answer) : ans = node
"""


# Doesn't work.
def inorder(self, root, k, counter, ans):
    if root:
        self.inorder(root.left, k, counter, ans)
        counter += 1
        if counter == k:
            ans = root.val
        self.inorder(root.right, k, counter, ans)


def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
    ans, counter = -1, 0
    self.inorder(root, k, counter, ans)
    return ans
