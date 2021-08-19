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
    NIL = RBTNode()

    def __init__(self):
        super().__init__()
        self.root = RBT.NIL

    @staticmethod
    def to_string(x):
        if x is not RBT.NIL:
            print(str(x.key) + "(", end='')
            RBT.to_string(x.left)
            print(", ", end='')
            RBT.to_string(x.right)
            print(")", end='')
        else:
            print("_", end='')

    def insert(self, key):
        y = RBT.NIL
        x = self.root
        z = RBTNode(key)

        while x is not RBT.NIL:
            y = x
            if x.key >= z.key:
                x = x.left
            else:
                x = x.right

        z.p = y
        if y is RBT.NIL:
            self.root = z
        elif y.key > z.key:
            y.left = z
        else:
            y.right = z

        z.colour = Colours.RED
        z.left = RBT.NIL
        z.right = RBT.NIL
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
        if y.left is not RBT.NIL:
            y.left.p = x

        y.p = x.p
        if x.p is RBT.NIL:
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

        if x.left is not RBT.NIL:
            x.left.p = x
        if x.p is RBT.NIL:
            self.root = y
        elif x is x.p.left:
            x.p.left = y
        else:
            x.p.right = y

        y.right = x
        x.p = y
