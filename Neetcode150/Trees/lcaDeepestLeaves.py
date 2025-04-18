# https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/description/?envType=daily-question&envId=2025-04-04

"""
1) Find max depth of tree (3 in this case)
2) Use recursion until you reach maxDepth - 1 and return that node.
"""

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


"""
root = [3,5,1,6,2,0,8,None,None,7,4]
          3 (depth=1)
         / \
        5   1  ← depth=2
       / \ / \
      6  2 0  8  ← depth=3
         / \
        7   4  ← depth=4 (deepest)

Returned: Node(2)

Step 1: maxDepth(root) = 4

Step 2: findDeepestParent(root, current_depth=1, target_depth=3)
Now we want to find the node at depth = 3, just above the deepest leaves.
"""


class Solution:
    def maxDepth(self, root):
        if not root:
            return 0
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        return 1 + max(left_depth, right_depth)

    def findNodeAtDepth(self, root, current_depth, target_depth):
        if not root:
            return None
        if current_depth == target_depth:
            return root  # LCA

        left = self.findNodeAtDepth(root.left, current_depth + 1, target_depth)
        right = self.findNodeAtDepth(root.right, current_depth + 1, target_depth)

        if left and right:  # this node is the common ancestor of two nodes below
            return root
        # only one side has the answer (else if only left return left, else return right)
        return left or right

    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        depth = self.maxDepth(root)
        return self.findNodeAtDepth(root, 1, depth - 1)


"""
Does not work : What if all the deepest leaves are not siblings (i.e., they don’t share the same parent)? For example:
      1
     /
    2
   / \
  4   5
       \
        6

Here, deepest leaf is 6, at depth 4. But its sibling is not another deepest leaf. So the LCA of all deepest leaves isn't at depth-1, 
it's where the left and right subtree have equal max depth — this could be deeper down or higher up depending on the structure.

So not only do we need to find the local LCA, but the global. How do I do this?

1) Identify deepest leaves and find the first node whose children are those deepest leaves.
"""


class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None  # root is optional
        # max depth
        self.candidate = None  # current LCA
        self.max_depth = -1
        self.dfs(root, 0)  # depth = 0
        return self.candidate

    def dfs(self, node, depth):
        if not node:
            return -1
        # either leaf node or inner node (continue DFS and check if that node is LCA)
        if not node.left and not node.right:  # leaf
            if depth > self.max_depth:
                self.candidate = node
                self.max_depth = depth
            return depth

        # inner node
        left_depth = self.dfs(node.left, depth + 1)
        right_depth = self.dfs(node.right, depth + 1)

        # depth of two children should be same AND it should also be the maximum depth (globally)
        if left_depth == right_depth == self.max_depth:
            # LCA found of current max depth
            self.candidate = node

        return max(left_depth, right_depth)


# Best Solution : Works in O(N)

"""
We use a recursive method to perform a depth-first search, recursively traversing each node in the tree and returning the maximum depth d of the current subtree and the lca node.
If the current node is null, we return depth 0 and an null node. In each search, we recursively search the left and right subtrees, and then compare the depths of the left and right subtrees:

If the left subtree is deeper, the deepest leaf node is in the left subtree, we return {left subtree depth + 1, the lca node of the left subtree}
If the right subtree is deeper, the deepest leaf node is in the right subtree, we return {right subtree depth + 1, the lca node of the right subtree}
If both left and right subtrees have the same depth and both have the deepest leaf nodes, we return {left subtree depth + 1, current node}.

Finally, we return the root node's lca node.
left[0] represents the maximum depth of the left subtree
left[1] represents the LCA node of the left subtree
    here we are returning 2 values
    we dont care about depth in the end, its just for making the above process easier
"""


class Solution:
    """
    dfs Returns: (max_depth, lca of deepest leaves in subtree rooted at node)

        # max depth of left right
         left_depth, right_depth = dfs(root.left), dfs(root.right)
         current_LCA_in_left_ST, current_LCA_in_right_ST = left_depth[1], right_depth[1]

    You compare integers directly (left_depth, right_depth)
    You return the deeper LCA, or the current node if both sides are equal

    """

    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(root):
            if not root:
                return 0, None
            left_d, current_LCA_in_left_ST = dfs(root.left)
            right_d, current_LCA_in_right_ST = dfs(root.right)
            if left_d > right_d:
                # left more
                return left_d + 1, current_LCA_in_left_ST
            if left_d < right_d:
                # right more
                return right_d + 1, current_LCA_in_right_ST
            # if both same : LCA found  (root) {doesn't matter what depth you increase (it's just to maintain track)}

            return left_d + 1, root

        return dfs(root)[1]  # lca return
