class BSTNode:
    def __init__(self, x=None):
        self.key = x
        self.right = None
        self.left = None
        self.p = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, z):
        y = None
        x = self.root
        z = BSTNode(z)

        while x is not None:
            y = x
            if x.key >= z.key:
                x = x.left
            else:
                x = x.right

        z.p = y
        if y is None:
            self.root = z
        elif y.key >= z.key:
            y.left = z
        else:
            y.right = z

    def delete(self, x):
        if x is None:
            return None
        elif x.right is None:
            self.transplant(x, x.left)
        elif x.left is None:
            self.transplant(x, x.right)
        else:
            y = BST.subtree_get_min(x.right)
            if y is not x.right:
                self.transplant(y, y.right)
                y.right = x.right
                x.right.p = y

            y.left = x.left
            x.left.p = y
            self.transplant(x, y)

    def search(self, x):
        node = self.root
        while node is not None and node.key != x:
            if node.key > x:
                node = node.left
            else:
                node = node.right

        if node is None:
            return False
        else:
            return True

    def to_string(self):
        def _to_string(x):
            if x is not None:
                print(str(x.key) + "(", end='')
                _to_string(x.left)
                print(", ", end='')
                _to_string(x.right)
                print(")", end='')
            else:
                print("_", end='')
        _to_string(self.root)

    def max(self):
        node = self.root
        while node is not None and node.right is not None:
            node = node.right

        if node is None:
            return None
        else:
            return node.key

    def get_max(self):
        node = self.root
        while node is not None and node.right is not None:
            node = node.right

        return node

    @staticmethod
    def subtree_get_max(x):
        node = x
        while node is not None and node.right is not None:
            node = node.right

        return node

    def min(self):
        node = self.root
        while node is not None and node.left is not None:
            node = node.left

        if node is None:
            return None
        else:
            return node.key

    @staticmethod
    def subtree_get_min(x):
        node = x
        while node is not None and node.left is not None:
            node = node.left

        return node

    def get_min(self):
        node = self.root
        while node is not None and node.left is not None:
            node = node.left

        return node

    def inorder_tree_walk(self):
        def _inorder_tree_walk(x):
            if x is not None:
                _inorder_tree_walk(x.left)
                print(str(x.key) + " ", end='')
                _inorder_tree_walk(x.right)

        _inorder_tree_walk(self.root)

    def successor(self, x):
        if x is None:
            return None
        elif x.right is not None:
            return BST.subtree_get_min(x.right)
        else:
            y = x
            while y is not self.root and y is y.p.right:
                y = y.p

            return y.p

    def predecessor(self, x):
        if x is None:
            return None
        elif x.left is not None:
            return BST.subtree_get_max(x.left)
        else:
            y = x
            while y is not self.root and y is y.p.left:
                y = y.p

            return y.p

    def transplant(self, x, v):
        if x is self.root:
            self.root = v
        elif x is x.p.left:
            x.p.left = v
        else:
            x.p.right = v

        if v is not None:
            v.p = x.p

    def get_height(self): # Many thanks to Apurva Sharma at https://favtutor.com/blogs/binary-tree-height
        def _get_height(x):
            if x is None:
                return 0
            else:
                left_height = _get_height(x.left)
                right_height = _get_height(x.right)

                return 1 + max(left_height, right_height)

        height = _get_height(self.root)
        if height == 0:
            return 0
        else:
            return height - 1
