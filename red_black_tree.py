from binary_search_tree import BST, BSTNode
from enum import auto, Enum


class Colours(Enum):
    BLACK = auto()
    RED = auto()


class RBTNode(BSTNode):
    def __init__(self, x='NIL', colour=Colours.BLACK):
        super().__init__(x)
        self.colour = colour


class RBT(BST):
    def __init__(self):
        super().__init__()
        self.NIL = RBTNode()
        self.root = self.NIL

    def to_string(self):
        def _to_string(x):
            if x is not self.NIL:
                print(str(x.key) + "(", end='')
                _to_string(x.left)
                print(", ", end='')
                _to_string(x.right)
                print(")", end='')
            else:
                print("_", end='')
        _to_string(self.root)

    def insert(self, key):
        y = self.NIL
        x = self.root
        z = RBTNode(key)

        while x is not self.NIL:
            y = x
            if x.key >= z.key:
                x = x.left
            else:
                x = x.right

        z.p = y
        if y is self.NIL:
            self.root = z
        elif y.key > z.key:
            y.left = z
        else:
            y.right = z

        z.colour = Colours.RED
        z.left = self.NIL
        z.right = self.NIL
        self.insert_fixup(z)

    def insert_fixup(self, z):
        while z.p.colour == Colours.RED:
            if z.p == z.p.p.left:
                y = z.p.p.right
                if y.colour == Colours.RED:
                    z.p.colour = Colours.BLACK
                    y.colour = Colours.BLACK
                    z.p.p.colour = Colours.RED
                    z = z.p.p
                else:
                    if z == z.p.right:
                        z = z.p
                        self.left_rotate(z)
                    z.p.colour = Colours.BLACK
                    z.p.p.colour = Colours.RED
                    self.right_rotate(z.p.p)
            else:
                y = z.p.p.left
                if y.colour == Colours.RED:
                    z.p.colour = Colours.BLACK
                    y.colour = Colours.BLACK
                    z.p.p.colour = Colours.RED
                    z = z.p.p
                else:
                    if z == z.p.left:
                        z = z.p
                        self.right_rotate(z)
                    z.p.colour = Colours.BLACK
                    z.p.p.colour = Colours.RED
                    self.left_rotate(z.p.p)
        self.root.colour = Colours.BLACK

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left is not self.NIL:
            y.left.p = x

        y.p = x.p
        if x.p is self.NIL:
            self.root = y
        elif x is x.p.left:
            x.p.left = y
        else:
            x.p.right = y

        y.left = x
        x.p = y

    def right_rotate(self, x):
        y = x.left
        x.left = y.right

        if y.right != self.NIL:
            y.right.p = x

        y.p = x.p
        if x.p is self.NIL:
            self.root = y
        elif x is x.p.right:
            x.p.right = y
        else:
            x.p.left = y
        y.right = x
        x.p = y

    def get_height(self):
        def _get_height(x):
            if x is self.NIL:
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
