# https://leetcode.com/problems/delete-nodes-and-return-forest/


class Solution:
    def __init__(self):
        self.ans = []

    def delNodes(
        self, root: Optional[TreeNode], to_delete: List[int]
    ) -> List[TreeNode]:
        if root.val not in to_delete:
            self.ans.append(root)
        # bfs
        q = [root]
        while q:
            node = q.pop(0)
            if node.val in to_delete:
                if node.left:
                    self.delNodes(node.left, to_delete)
                if node.right:
                    self.delNodes(node.right, to_delete)
            else:
                if node.left:
                    q.append(node.left)
                    if node.left.val in to_delete:
                        node.left = None
                if node.right:
                    q.append(node.right)
                    if node.right.val in to_delete:
                        node.right = None
        return self.ans
