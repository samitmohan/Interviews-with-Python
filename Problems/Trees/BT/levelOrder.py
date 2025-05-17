import collections


# https://leetcode.com/problems/binary-tree-level-order-traversal/

#      1
#     / \
#    2    3
#   / \  / \
#  4   5 6  7

# ans = [[1],[2,3],[4,5,6,7]]


# Logic : BFS using Queue : While queue is not empty, check for left and right nodes
#  if left child exists, push in queue, if right child exists push in queue
#  once exploration of one level is over, put that level in ans

# ans : array of array : O(N)
# Run BFS : How to do BFS? Queue. Keep doing it until queue is empty : Pop element add to list and move to next level (check if left and right child nodes exist)
# package all the sublists into one listj:w


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = 0
        q = collections.deque([root] if root else [])
        while q:
            level = []
            size = len(q)
            for i in range(size):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)
            ans.append(level)
        return ans


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        if not root:
            return ans
        q = collections.deque()
        q.append(root)  # add root element
        while q:
            size = len(q)
            level = []  # sub-list
            for i in range(size):
                node = q.popleft()  # pop first element and store it in level (of size 1) then for level 2 : add node.left and node.right and store it in level sublist then for size 3...
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

                level.append(node.val)  # add to sublist

            ans.append(level)
        return ans


# or
# node = q.popleft()
# if node:
#   level.append(node.val)
#   ans.append(node.left)
#   ans.append(node.right)
# if level: # if level = 0 for empty : then no point
#   ans.append(level)
