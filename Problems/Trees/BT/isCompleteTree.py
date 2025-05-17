# https://leetcode.com/problems/check-completeness-of-a-binary-tree/
from collections import deque


# Simple BFS
# no node should be null in between non-null nodes : if yes -> not a complete binary tree.
# Keep track of null nodes : nullNodeFound (false init)
# in BFS:
# if node == null : mark as true
# else -> if not, check if we have already visited a null node
# if node != null and nullNodeFound already true : FALSE answer
# push node.left and node.right and continue BFS
# return True in the end


class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        nullNodeFound = False
        if root == None:
            return True  # empty tree : always a complete BT
        q = deque([root])
        while q:
            node = q.popleft()
            if node == None:
                nullNodeFound = True
            else:
                # current node isn't null -> check if we've already found a nulll node : if yes -> can't be possible
                # else -> check for node.left and node.right (BFS)
                if nullNodeFound:
                    return False
                q.append(node.left)
                q.append(node.right)
        return True
