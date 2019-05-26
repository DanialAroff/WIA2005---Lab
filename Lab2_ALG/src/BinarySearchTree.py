class TreeNode:
    def __init__(self, data=None):
        self.data = data
        self.right = None
        self.left = None


class BST:
    def __init__(self):
        self.root = None

    def get_root(self):
        return self.root

    def insert(self, data):
        parent = None
        if self.root is None:
            self.root = TreeNode(data)
        else:
            current = self.root
            while current is not None:
                if data < current.data:
                    parent = current
                    current = current.left
                elif data > current.data:
                    parent = current
                    current = current.right
            if data < parent.data:
                parent.left = TreeNode(data)
            elif data > parent.data:
                parent.right = TreeNode(data)

    def search(self, data):
        current = self.root
        while current is not None:
            if data < current.data:
                current = current.left
            elif data > current.data:
                current = current.right
            else:
                return True
        return False

    def min_value_node(self):
        """To find the node with minimum value within a tree"""
        current = self.root
        while current.left is not None:
            current = current.left
        return current.data

    def delete(self, data):
        parent = current = self.root
        while current is not None:
            if data < current.data:
                parent = current
                current = current.left
            elif data > current.data:
                parent = current
                current = current.right
            else:
                # if node does not have a left child
                if current.left is None:
                    parent.left = current.right
                    break

                # if node has left child
                elif current.left is not None:
                    temp = current.left
                    while temp.right is not None:
                        parent_temp = temp
                        temp = temp.right
                    current.data = temp.data

                    # connect the parent of rightmost node to
                    # the left child of rightmost node
                    parent_temp.right = temp.left

    def inorder(self):
        """a function which mainly calls the inorderRec function"""
        self.inorderRec(self.root)

    def inorderRec(self, root):
        """print the content with in-order traversal"""
        if root:
            self.inorderRec(root.left)
            print(root.data)
            self.inorderRec(root.right)
