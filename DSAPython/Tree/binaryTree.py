"""
    5
   / \
  3   7
 /     \
1       9
"""


class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data, current_node):
        if data < current_node.data:
            if current_node.left is None:
                current_node.left = Node(data)
            else:
                self._insert(data, current_node.left)
        elif data > current_node.data:
            if current_node.right is None:
                current_node.right = Node(data)
            else:
                self._insert(data, current_node.right)
        else:
            print("Value already in tree.")


# Inorder : L N R
# Preorder : N L R
# Postorder : L R N


def inorder_traversal(node):
    if node:
        inorder_traversal(node.left)
        print(node.data)
        inorder_traversal(node.right)


def preorder_traversal(node):
    if node:
        print(node.data)
        inorder_traversal(node.left)
        inorder_traversal(node.right)


def postorder_traversal(node):
    if node:
        inorder_traversal(node.left)
        inorder_traversal(node.right)
        print(node.data)


def levelorder_traversal(node):
    if node:
        q = [node]
        while q:
            node_val = q.pop(0)
            print(node_val.data)

            if node_val.left:
                q.append(node_val.left)

            if node_val.right:
                q.append(node_val.right)


tree = BinaryTree()
tree.insert(5)
tree.insert(3)
tree.insert(7)
tree.insert(1)
tree.insert(9)
inorder_traversal(tree.root)
levelorder_traversal(tree.root)
