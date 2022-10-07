import unittest
import itertools
import random
from sorting import *

SEED = 12345

def checkAscending(target_list):
    return all(target_list[i] <= target_list[i+1]
                    for i in range(len(target_list)-1))


class TestSorting(unittest.TestCase):
    def setUp(self):
        # We want the lists generated to be random
        # but failed test cases also needs to be reproducible 
        random.seed(SEED)


    # Template for testing
    def template(self, func):
        # Test sorting on empty list
        target = []
        func([])
        self.assertEqual(target, [])
        
        # Test sorting from list size 1 to 100
        # 5 times each for each size
        for n in range(1, 100):
            for _ in range(1, 5):
                target = random.choices(range(1,1000), k=n)
                func(target)
                self.assertTrue(checkAscending(target))
    
    def test_bubble(self):
        self.template(bubble_sort)

    def test_insertion(self):
        self.template(insertion_sort)

    
if __name__ == "__main__":
    unittest.main()