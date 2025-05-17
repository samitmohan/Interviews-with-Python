# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/

"""
Postorder : Left Right Root
Inorder : Left Root Right
First node will always be last element of PO (Root)
To find remaining values : Use Inorder

Inorder : 40,20,50,10,60,30
Postorder : 40,50,20,60,30,10

10 -> root
In Inorder : 40,20,50 (left ST) and 60,30 (right ST)

Now :
Inorder: 40,20,50
Postorder : 40,50,20

Same question : 20 becomes the root and to find other values : use Inorder.
Recursive solution

inorder = [9, 3, 15, 20, 7]
postorder = [9, 15, 7, 20, 3]

root = buildTree(inorder, postorder)

    3
   / \
  9  20
    /  \
   15   7

O(N^2) : instead of looking up root_index all the time (O(N) operation) : save it in hm.
inorder_index_hm = {v:i for i, v in enumerate(inorder)}
        root_index = inorder_index[root.val]
"""


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder:
            return None  # can still work if just PO given : root
        root_val = postorder.pop()
        root = TreeNode(root_val)  # root will always be of PO
        # find index of root in IO (elements left to this : left ST and right to this : right ST)
        root_index = inorder.index(root_val)

        # recursively building tree
        root.right = self.buildTree(inorder[root_index + 1 :], postorder)
        root.left = self.buildTree(inorder[:root_index], postorder)

        return root
