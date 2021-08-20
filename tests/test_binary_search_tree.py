import unittest
import io
import sys
from binary_search_tree import BST, BSTNode


class TestInsert(unittest.TestCase):
    def test_insert(self):
        bst = BST()
        bst.insert(4)
        self.assertEqual(bst.root.key, 4)
        self.assertEqual(bst.root.left, None)
        self.assertEqual(bst.root.right, None)
        bst.insert(5)
        self.assertEqual(bst.root.right.key, 5)
        bst.insert(3)
        self.assertEqual(bst.root.left.key, 3)
        bst.insert(1)
        self.assertEqual(bst.root.left.left.key, 1)
        bst.insert(9)
        self.assertEqual(bst.root.right.right.key, 9)


class TestBSTMainFuncts(unittest.TestCase):
    def setUp(self):
        self.bst = BST()
        self.bst.insert(4)
        self.bst.insert(3)
        self.bst.insert(7)
        self.bst.insert(5)
        self.bst.insert(1)
        self.bst.insert(13)
        self.bst.insert(2)
        self.bst.insert(-1)

    def test_to_string(self):
        captured_output = io.StringIO()
        sys.stdout = captured_output
        self.bst.to_string()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), "4(3(1(-1(_, _), 2(_, _)), _), 7(5(_, _), 13(_, _)))")

    def test_search(self):
        self.assertEqual(self.bst.search(-1), True)
        self.assertEqual(self.bst.search(4), True)
        self.assertEqual(self.bst.search(5), True)
        self.assertEqual(self.bst.search(24), False)

    def test_max(self):
        self.assertEqual(self.bst.max(), 13)

    def test_get_max(self):
        self.assertEqual(self.bst.get_max().key, 13)

        bst1 = BST()
        self.assertEqual(bst1.get_max(), None)
        bst1.insert(4)
        self.assertEqual(bst1.get_max().key, 4)

    def test_subtree_get_max(self):
        node = self.bst.root.left
        self.assertEqual(BST.subtree_get_max(node).key, 3)
        self.assertEqual(BST.subtree_get_max(self.bst.root), self.bst.get_max())

    def test_min(self):
        self.assertEqual(self.bst.min(), -1)

    def test_get_min(self):
        self.assertEqual(self.bst.get_min().key, -1)

        bst1 = BST()
        self.assertEqual(bst1.get_min(), None)
        bst1.insert(4)
        self.assertEqual(bst1.get_min().key, 4)

    def test_subtree_get_min(self):
        node = self.bst.root.right
        self.assertEqual(BST.subtree_get_min(node).key, 5)
        self.assertEqual(BST.subtree_get_min(self.bst.root), self.bst.get_min())

    def test_inorder_tree_walk(self):
        self.bst.insert(1)
        self.bst.insert(5)
        captured_output = io.StringIO()
        sys.stdout = captured_output
        self.bst.inorder_tree_walk()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), "-1 1 1 2 3 4 5 5 7 13 ")

    def test_successor(self):
        self.assertEqual(self.bst.successor(self.bst.root).key, 5)
        self.assertEqual(self.bst.successor(self.bst.root.right.right), None)
        self.assertEqual(self.bst.successor(self.bst.root.left.left.left).key, 1)

        bst1 = BST()
        self.assertEqual(bst1.successor(bst1.root), None)

    def test_predecessor(self):
        self.assertEqual(self.bst.predecessor(self.bst.root).key, 3)
        self.assertEqual(self.bst.predecessor(self.bst.root.left.left.left), None)
        self.assertEqual(self.bst.predecessor(self.bst.root.right).key, 5)

        bst1 = BST()
        self.assertEqual(bst1.predecessor(bst1.root), None)

    def test_transplant(self):
        v = BSTNode(2)
        v.left = BSTNode(1)
        v.right = BSTNode(3)
        x = self.bst.root.left

        self.bst.transplant(x, v)
        self.assertEqual(self.bst.root.left.key, 2)
        self.assertEqual(self.bst.root.left.left.key, 1)
        self.assertEqual(self.bst.root.left.right.key, 3)

        bst2 = BST()
        bst2.insert(2)
        bst2.transplant(bst2.root, v)
        self.assertEqual(bst2.root.key, 2)
        self.assertEqual(bst2.root.left.key, 1)
        self.assertEqual(bst2.root.right.key, 3)

    def test_delete(self):
        self.bst.delete(self.bst.root)
        root = self.bst.root
        self.assertEqual(root.key, 5)
        self.assertEqual(root.left.key, 3)
        self.assertEqual(root.right.key, 7)
        self.assertEqual(root.left.left.key, 1)

        self.setUp()
        self.bst.delete(self.bst.root.right.left)
        self.assertEqual(self.bst.root.right.left, None)

        bst1 = BST()
        self.assertEqual(bst1.delete(bst1.root), None)

    def test_height(self):
        self.bst.insert(1)
        self.bst.insert(5)
        self.assertEqual(self.bst.get_height(), 4)

        bst1 = BST()
        self.assertEqual(bst1.get_height(), 0)
        bst1.insert(1)
        self.assertEqual(bst1.get_height(), 0)
        bst1.insert(2)
        self.assertEqual(bst1.get_height(), 1)


if __name__ == "__main__":
    unittest.main()
