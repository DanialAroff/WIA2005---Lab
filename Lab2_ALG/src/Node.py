class Node:
    def __init__(self, data):
        self.right = None
        self.left = None
        self.data = data

    def insert(self, data):
        """
        Insert new node with data
        :param data:
        :return nothing:
        """
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def lookup(self, data, parent = None):
        """
        Lookup node containing data
        :param data:
        :param parent:
        :return node and node's parent if found or None, None:
        """
        if data < self.data:
            if self.left is None:
                return None, None
            return self.left.lookup(data, self)
        elif data > self.data:
            if self.right is None:
                return None, None
            return self.right.lookup(data, self)
        else:
            return self, parent

    def delete(self, data):
        """

        :param data:
        :return:
        """
        node, parent = self.lookup(data)
        if node is not None:
            
