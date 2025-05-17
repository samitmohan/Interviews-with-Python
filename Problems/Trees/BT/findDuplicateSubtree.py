# https://leetcode.com/problems/find-duplicate-subtrees/description/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
Hashmap to store serialised node -> [list of nodes it has]
   1
 /  \
2    3

preorder traversal -> 1,2,3 (in list) [as a string]
better way : 1,2,N,N,3,N,N
if there are more than same subtree : len(subtree hashmap) == 1 [already seen before] : add to answer

Steps: dfs -> build hashmap (serialised tree string) -> if seen before -> add to answer -> return answer
"""


class Solution:
    def findDuplicateSubtrees(
        self, root: Optional[TreeNode]
    ) -> List[Optional[TreeNode]]:
        subtree = defaultdict(list)

        def preorder(root):
            if not root:
                return "null"
            s = ",".join([str(root.val), preorder(root.left), preorder(root.right)])
            if len(subtree[s]) == 1:  # answer found
                ans.append(root)

            subtree[s].append(root)
            return s

        ans = []
        preorder(root)
        return ans
