# Node structure
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

# Binary Search Tree
class BST:
    def __init__(self):
        self.root = None

    # Insert a new key
    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, node, key):
        if key < node.key:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert(node.left, key)
        elif key > node.key:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert(node.right, key)

    # Search for a key
    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if node is None or node.key == key:
            return node
        if key < node.key:
            return self._search(node.left, key)
        return self._search(node.right, key)

    # In-order Traversal (sorted order)
    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.key, end=" ")
            self.inorder(node.right)

# Example usage
tree = BST()
for val in [8, 3, 10, 1, 6, 14, 4, 7, 13]:
    tree.insert(val)

print("Inorder Traversal (sorted):")
tree.inorder(tree.root)

print("\nSearch for 7:", "Found" if tree.search(7) else "Not Found")
print("Search for 2:", "Found" if tree.search(2) else "Not Found")
