# https://leetcode.com/problems/binary-tree-right-side-view/

"""
iterative bfs(queue FIFO), add prev level which doesn't have any nulls to the result;
Time & Space : O(n)
Level order traversal / BFS : for each level we want the right most node
[1] : 1
[2,3]: 3
[5,4] : 4
[7] : 7 (imaginary node on left)
queue : bfs (before popping take left and right child)
ans : add rightmost values in queue to this

"""


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = collections.deque([root] if root else [])
        ans = []
        while q:
            right_side = None
            size = len(q)  # size of queue
            for i in range(size):
                node = q.popleft()
                right_side = node
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if right_side:  # not null
                ans.append(right_side.val)
        return ans


# Another solution (Neetcode way)
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = collections.deque([root] if root else [])
        ans = []
        while q:
            right_side = None
            size = len(q)  # size of queue
            for i in range(size):
                node = q.popleft()
                if node:
                    right_side = node
                    q.append(node.left)
                    q.append(node.right)
            if right_side:
                ans.append(right_side.val)
        return ans
