from heap import MinHeap
import random
import unittest

SEED = 12345
random.seed(SEED)

class TestMinHeap(unittest.TestCase):
    def setUp(self):
        self.minheap = MinHeap()

    def _assert_MHP_helper(self, root):
        if (root == None): return
        if (root.left != None):
            self.assertLessEqual(root.value, root.left.value)
            self._assert_MHP_helper(root.left)
        if (root.right != None):
            self.assertLessEqual(root.value, root.right.value)
            self._assert_MHP_helper(root.right)

    def assert_min_heap_property(self):
        self._assert_MHP_helper(self.minheap.root)

    def test_heap(self):
        for i in range(0, 100):
            self.minheap.insert(random.randint(1, 100))
            self.assert_min_heap_property()
        
        x = 0
        for i in range(0, 100):
            y = self.minheap.deleteMin()
            self.assertGreaterEqual(y, x)
            self.assert_min_heap_property()
            x = y

if __name__ == "__main__":
    pass