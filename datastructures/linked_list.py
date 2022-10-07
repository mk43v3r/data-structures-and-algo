class Node:
    def __init__(self, value, next):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self):
        self._start = None
        self._end = None

    # Generator for iterating through nodes in the linked list
    def iterator(self):
        curr = self._start
        while curr != None:
            yield curr
            curr = curr.next
    
    # Create a node from the value and insert at the front
    def insert(self, value):
        node = Node(value, self._start)

        if (self._start == None):
            self._start = self._end = node
            return
        
        self._start = node 

    # Create a node from the value and append it at the back
    def append(self, value):
        node = Node(value, None)

        if (self._end == None):
            self._start = self._end = node
            return

        self._end.next = node
        self._end = node

    # Remove the last node and returns it
    def pop(self):
        if (self._start == None):
            return None
        elif (self._start == self._end):
            temp = self._start
            self._start = self._end = None
            return temp

        prev, curr = None, self._start

        while (curr.next != None):
            prev = curr
            curr = curr.next
        
        prev.next = None
        self._end = prev
        return curr
    
    # Remove the first node and returns it
    def remove(self):
        if (self._start == None):
            return None
        elif (self._start == self._end):
            temp = self._start
            self._start = self._end = None
            return temp
        
        temp = self._start
        self._start = self._start.next
        return temp

class Stack:
    def __init__(self):
        self._linkedlist = LinkedList()

    def push(self, value):
        self._linkedlist.append(value)

    def pop(self):
        node = self._linkedlist.pop()
        if (not node):
            raise Exception("Attempting to pop from empty stack.")
        return node.value

class Queue:
    def __init__(self):
        self._linkedlist = LinkedList()

    def queue(self, value):
        self._linkedlist.append(value)

    def dequeue(self):
        node = self._linkedlist.remove()
        if (not node):
            raise Exception("Attempting to dequeue from empty queue.")
        return node.value
            