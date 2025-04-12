# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/description/

# preorder and seperate by , when null reached : represented by N to create string
# use preorder traversal on string to create Tree
# if both children null : base case
# O(n)

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        ans = []  # ["1", "2", "3"] and join by comma

        def preorder(root):
            if not root:
                ans.append("N")
                return
            ans.append(str(root.val))
            preorder(root.left)
            preorder(root.right)

        preorder(root)
        return ",".join(ans)

    def deserialize(self, data):
        """Decodes your encoded data (string) to tree.

        :type data: str
        :rtype: TreeNode
        """
        vals = data.split(",")
        self.i = 0  # member of class (tells the current index node)

        def preorder():
            # base case -> both child N
            if vals[self.i] == "N":
                self.i += 1
                return None
            root = TreeNode(int(vals[self.i]))  # create tree node from the string
            self.i += 1  # next val
            root.left = preorder()
            root.right = preorder()
            return root

        return preorder()

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
