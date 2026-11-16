# Binary Search Tree: insert, search, traversals, and delete.


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BST:
    def insert(self, root, key):
        if root is None:
            return Node(key)
        if key < root.key:
            root.left = self.insert(root.left, key)
        elif key > root.key:
            root.right = self.insert(root.right, key)
        return root

    def search(self, root, key):
        if root is None or root.key == key:
            return root
        if key < root.key:
            return self.search(root.left, key)
        return self.search(root.right, key)

    def min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def delete(self, root, key):
        if root is None:
            return None
        if key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            if root.left is None:
                return root.right
            if root.right is None:
                return root.left
            successor = self.min_value_node(root.right)
            root.key = successor.key
            root.right = self.delete(root.right, successor.key)
        return root

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.key, end=" ")
            self.inorder(root.right)

    def preorder(self, root):
        if root:
            print(root.key, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)


def main():
    bst = BST()
    root = None
    keys = input("Enter keys separated by spaces: ").split()

    for value in keys:
        root = bst.insert(root, int(value))

    print("In-order Traversal:")
    bst.inorder(root)
    print()
    print("Preorder Traversal:")
    bst.preorder(root)
    print()

    target = int(input("Enter key to search: "))
    if bst.search(root, target):
        print(f"Key {target} found in BST.")
    else:
        print(f"Key {target} not found in BST.")

    target = int(input("Enter key to delete: "))
    root = bst.delete(root, target)
    print(f"In-order after deleting {target}:")
    bst.inorder(root)
    print()


if __name__ == "__main__":
    main()
