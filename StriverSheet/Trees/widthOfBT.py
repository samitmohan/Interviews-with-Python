# https://leetcode.com/problems/maximum-width-of-binary-tree/

from collections import deque
class Solution:
    def widthOfBinaryTree(self, root):
        '''
        Use BFS (deque) with a tuple: (node, index)
        For each level:
            Store first_index and last_index
            Track max width: last_index - first_index + 1
        For each node:
            If left exists → enqueue (node.left, 2 * index)
            If right exists → enqueue (node.right, 2 * index + 1)
        '''
        if not root: 
            return 0
        ans = 0
        q = deque([(root, 0)]) # node and index
        while q:
            level_length = len(q)
            _, first_idx = q[0]
            _, last_idx = q[-1]
            ans = max(ans, last_idx-first_idx+1)
            for _ in range(level_length):
                node, idx = q.popleft()
                if node.left:
                    q.append((node.left, 2 * idx))
                if node.right:
                    q.append((node.right, 2 * idx + 1))

        return ans