from binary_tree import *
import random
import unittest

SEED = 12345
class TestBinarySearchTree(unittest.TestCase):
    def setUp(self):
        random.seed(SEED)
        self.tree = BinarySearchTree()
    
    # Test that the left child node is lesser or equal to the parent
    # and the right child node is greater than the parent
    def helper(self, node):
        if (node.left != None):
            self.assertLessEqual(node.left.value, node.value)
            self.helper(node.left)
        if (node.right != None):
            self.assertGreaterEqual(node.right.value, node.value)
            self.helper(node.right)
    
    def test_binary_search_tree(self):
        for _ in range(100):    # Test against 100 randomly lists with 30 elements
            self.tree = BinarySearchTree()
            L = random.choices(range(1,1000), k=30)
            for i in range(30):
                # Insert 30 elements in order
                self.tree.insert(L[i])
                # Check that the binary search tree property holds
                self.helper(self.tree.root)
            for i in range(30):
                n = random.choice(L)
                L.remove(n)
                self.tree.delete(n)
                self.helper(self.tree.root)


if __name__ == "__main__":
    unittest.main()