from hashmap import *
import unittest

class TestHashMap(unittest.TestCase):
    def setUp(self):
        self.hashmap = HashMap(lambda x: (x >> 10)**2, 10)

    def test_insert(self):
        # Test basic insert functionality
        self.hashmap.insert(0, 0)

        # Test  that inserting can exceed array size and that
        # collision is resolved properly by linked list chaining
        for n in range(1, 100):
            self.hashmap.insert(n, n)

        # Test that inserting (key, value) with the same key
        # raises an Exception
        for n in range(1, 100):
            with self.assertRaises(Exception):
                self.hashmap.insert(n, n)

    def test_find(self):
        for n in range(1, 100):
            self.hashmap.insert(n, n**2)
        
        # Test that elements in the hashmap are found and
        # the value is returned
        for n in range(1, 100):
            self.assertEqual(self.hashmap.find(n), n**2)

        # Test that elements not in the hashmap are not found and
        # None is returned
        for n in range(100, 200):
            self.assertEqual(self.hashmap.find(n), None)

    def test_delete(self):
        for n in range(1, 100):
            self.hashmap.insert(n, n)

        # Test that elements in the hashmap are deleted
        for n in range(1, 50):
            self.assertEqual(self.hashmap.delete(n).value[0], n)
        
        # Test that elements not in the hashmap are not deleted
        for n in range(100, 200):
            self.assertEqual(self.hashmap.delete(n), None)

        # Test deleting every elements
        for n in range(50, 100):
            self.assertEqual(self.hashmap.delete(n).value[0], n)