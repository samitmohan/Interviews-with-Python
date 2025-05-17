# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/

"""
2 Observations
1. 1st value in preorder list : always ROOT. 
    3
   /  \
  9    20
      /  \
     15    7
preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
now preorder = [9,20,15,7] : 1st value always root -> take sublist -> do it again recursively

2. How to know what value goes to left and right side? inorder list.
  Once root identified from preorder, locate the same in inorder : [9,   3,   15,20,7] : index : 1 # mid
    all values <- 3 are on left and -> 3 are on right of tree.
      partition the array in a similar way. [9    20,15,7] now recursively solve : root = 9, and then root = 20, locate value in inorder form parition L and R : solve again.
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder, inorder):
        if not preorder or not inorder:
            return None
        root = TreeNode(preorder[0])  # root will always be 1st val of preorder
        # locate that value in inorder = mid
        mid = inorder.index(preorder[0])
        # partition left and right
        # left : 1 - mid for both PO and IO (why 1? because first element in preorder is root)
        # ruight : mid - end for both PO and IO
        root.left = self.buildTree(preorder[1 : mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid + 1 :], inorder[mid + 1 :])

        return root
