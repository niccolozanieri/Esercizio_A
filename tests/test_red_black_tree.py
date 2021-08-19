import unittest
import io
import sys
from red_black_tree import RBT, RBTNode, Colours


class TestInsert(unittest.TestCase):
    def test_insert(self):
        rbt = RBT()
        rbt.insert(10)
        rbt.insert(9)
        rbt.insert(8)
        rbt.insert(7)
        rbt.insert(6)

        captured_output = io.StringIO()
        sys.stdout = captured_output
        RBT.to_string(rbt.root)
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), "9(7(6(_, _), 8(_, _)), 10(_, _))")

        self.assertEqual(rbt.root.colour, Colours.BLACK)
        self.assertEqual(rbt.root.left.colour, Colours.BLACK)
        self.assertEqual(rbt.root.left.left.colour, Colours.RED)
        self.assertEqual(rbt.root.left.right.colour, Colours.RED)
        self.assertEqual(rbt.root.right.colour, Colours.BLACK)


class TestRotations(unittest.TestCase):
    def setUp(self):
        self.rbt = RBT()
        self.rbt.insert(4)
        self.rbt.insert(2)
        self.rbt.insert(7)
        self.rbt.insert(5)
        self.rbt.insert(13)
        self.rbt.insert(1)
        self.rbt.insert(3)

    def test_left_rotate(self):
        self.rbt.left_rotate(self.rbt.root)
        captured_output = io.StringIO()
        sys.stdout = captured_output
        RBT.to_string(self.rbt.root)
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), "7(4(2(1(_, _), 3(_, _)), 5(_, _)), 13(_, _))")

    def test_right_rotate(self):
        self.rbt.right_rotate(self.rbt.root.left)
        captured_output = io.StringIO()
        sys.stdout = captured_output
        RBT.to_string(self.rbt.root)
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), "4(1(_, 2(_, 3(_, _))), 7(5(_, _), 13(_, _)))")


if __name__ == "__main__":
    unittest.main()
