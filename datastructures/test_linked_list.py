from linked_list import *
import unittest

class TestLinkedList(unittest.TestCase):
    def setUp(self):
        self.linkedlist = LinkedList()

    def test_iterator(self):
        # Test empty linked list iteration
        for _ in self.linkedlist.iterator():
            self.assertTrue(False)
        
        # Test for size increase
        self.linkedlist.append(1)
        self.assertEqual(len(list(self.linkedlist.iterator())), 1)

        self.linkedlist.append(2)
        self.assertTrue(len(list(self.linkedlist.iterator())), 2)

        # Test that the iterated type is Node
        for n in self.linkedlist.iterator():
            self.assertEqual(type(n), Node)

        # Test for size decrease
        self.linkedlist.pop()
        self.assertEqual(len(list(self.linkedlist.iterator())), 1)

        self.linkedlist.pop()
        self.assertEqual(len(list(self.linkedlist.iterator())), 0)
    
    def test_case(self):
        self.linkedlist.append(1)
        self.assertEqual(list(n.value for n in self.linkedlist.iterator()),
                                [1])

        self.linkedlist.insert(2)
        self.assertEqual(list(n.value for n in self.linkedlist.iterator()),
                                [2, 1])

        self.linkedlist.append(3)
        self.assertEqual(list(n.value for n in self.linkedlist.iterator()),
                                [2,1,3])

        self.linkedlist.insert(4)
        self.assertEqual(list(n.value for n in self.linkedlist.iterator()),
                                [4,2,1,3])
        
        x = self.linkedlist.pop().value
        self.assertEqual(x, 3)
        self.assertEqual(list(n.value for n in self.linkedlist.iterator()),
                                [4,2,1])

        x = self.linkedlist.remove().value
        self.assertEqual(x, 4)
        self.assertEqual(list(n.value for n in self.linkedlist.iterator()),
                                [2,1])
        
        x = self.linkedlist.pop().value
        self.assertEqual(x, 1)
        self.assertEqual(list(n.value for n in self.linkedlist.iterator()),
                                [2])

        x = self.linkedlist.remove().value
        self.assertEqual(x, 2)
        self.assertEqual(list(n.value for n in self.linkedlist.iterator()),
                                [])
        
        self.assertEqual(self.linkedlist.remove(), None)
        self.assertEqual(self.linkedlist.pop(), None)

class TestStack(unittest.TestCase):
    def setUp(self):
        self.stack = Stack()

    def test_all(self):
        # Test general property of stack: LIFO
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)
        self.assertEqual(self.stack.pop(), 3)
        self.assertEqual(self.stack.pop(), 2)
        self.assertEqual(self.stack.pop(), 1)
        # Attempting to pop empty stack
        self.assertRaises(Exception, self.stack.pop)    

class TestQueue(unittest.TestCase):
    def setUp(self):
        self.queue = Queue()

    def test_all(self):
        # Test general property of queue: FIFO
        self.queue.queue(1)
        self.queue.queue(2)
        self.queue.queue(3)
        self.assertEqual(self.queue.dequeue(), 1)
        self.assertEqual(self.queue.dequeue(), 2)
        self.assertEqual(self.queue.dequeue(), 3)
        # Attempting to dequeue empty queue
        self.assertRaises(Exception, self.queue.dequeue)

if __name__ == "__main__":
    unittest.main()