class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert_recursive(data, self.root)

    def _insert_recursive(self, data, current_node):
        if data < current_node.data:
            if current_node.left is None:
                current_node.left = Node(data)
            else:
                self._insert_recursive(data, current_node.left)
        elif data > current_node.data:
            if current_node.right is None:
                current_node.right = Node(data)
            else:
                self._insert_recursive(data, current_node.right)

    def search(self, data):
        return self._search_recursive(data, self.root)

    def _search_recursive(self, data, current_node):
        if current_node is None or current_node.data == data:
            return current_node
        if data < current_node.data:
            return self._search_recursive(data, current_node.left)
        return self._search_recursive(data, current_node.right)

    def delete(self, data):
        self.root = self._delete_recursive(data, self.root)

    def _delete_recursive(self, data, current_node):
        if current_node is None:
            return current_node

        if data < current_node.data:
            current_node.left = self._delete_recursive(data, current_node.left)
        elif data > current_node.data:
            current_node.right = self._delete_recursive(data, current_node.right)
        else:
            if current_node.left is None:
                return current_node.right
            elif current_node.right is None:
                return current_node.left

            min_node = self._find_minimum(current_node.right)
            current_node.data = min_node.data
            current_node.right = self._delete_recursive(min_node.data, current_node.right)

        return current_node

    def _find_minimum(self, current_node):
        while current_node.left is not None:
            current_node = current_node.left
        return current_node

    def inorder_traversal(self):
        self._inorder_recursive(self.root)

    def _inorder_recursive(self, current_node):
        if current_node:
            self._inorder_recursive(current_node.left)
            print(current_node.data, end=" ")
            self._inorder_recursive(current_node.right)


# Usage example:
binary_tree = BinaryTree()
binary_tree.insert(50)
binary_tree.insert(30)
binary_tree.insert(20)
binary_tree.insert(40)
binary_tree.insert(70)
binary_tree.insert(60)
binary_tree.insert(80)

binary_tree.inorder_traversal()  # Output: 20 30 40 50 60 70 80

binary_tree.delete(30)
binary_tree.inorder_traversal()  # Output: 20 40 50 60 70 80
