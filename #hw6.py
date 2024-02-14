#hw6
class TreeNode:
    def __init__(self, key): # intializes a tree node with a key value
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self): # intializes an enpty binary search tree
        self.root = None

    def insert(self, key): # inserts a new key into the binary search tree
        self.root = self._insert(self.root, key)

    def _insert(self, root, key): # recursively inserts a new key into the binary search tree
        if root is None:
            return TreeNode(key)
        if key < root.key:
            root.left = self._insert(root.left, key)
        else:
            root.right = self._insert(root.right, key)
        return root # returns the root node of the updated subtree

    def preOrderl(self): # performs a pre-order traversal of the binary ssearch tree
        self._preOrder(self.root)

    def _preOrder(self, node): # recursively performs a pre-order traversal of the binary search tree
        if node:
            print(node.key, end=" ")
            self._preOrder(node.left)
            self._preOrder(node.right)

    def inOrder(self): # perforns an in-order traversal
        self._inOrder(self.root)

    def _inOrder(self, node): # recursively performs an in-order traversal
        if node:
            self._inOrder(node.left)
            print(node.key, end=" ")
            self._inOrder(node.right)

    def postOrder(self): # performs  a post-order traversal
        self._postOrder(self.root)

    def _postOrder(self, node): # recursively performs a post-order traversal
        if node:
            self._postOrder(node.left)
            self._postOrder(node.right)
            print(node.key, end=" ")

# Example usage:
bst = BinarySearchTree()
keys = [5, 3, 8, 2, 4, 7, 9]
for key in keys:
    bst.insert(key)

print("Pre-order traversal:")
bst._preOrder()
print("\nIn-order traversal:")
bst.inOrder()
print("\nPost-order traversal:")
bst.postOrder()
