from binary_tree import Node, BinaryTree

# Minimizing Heap implemented with nodes
class MinHeap(BinaryTree):
    def _insert_helper(self, root, value):
        if (value < root.value):
            temp = root.value
            root.value = value
            self._insert_helper(root, temp)
        else:
            if (root.left == None):
                root.left = Node(value)
            elif (root.right == None):
                root.right = Node(value)
            else:
                self._insert_helper(root.left, value)

    def insert(self, value):
        if (self.root == None):
            self.root = Node(value)
        else:
            self._insert_helper(self.root, value)

    # Remove the minimum from the heap and returns the value
    def deleteMin(self):
        if (self.root == None): return None

        min = self.root.value

        prev, curr = None, self.root
        while (curr.left != None or curr.right != None):
            prev = curr
            if (curr.left == None):
                curr.value = curr.right.value
                curr = curr.right
            elif (curr.right == None):
                curr.value = curr.left.value
                curr = curr.left
            elif (curr.left.value < curr.right.value):
                curr.value = curr.left.value
                curr = curr.left
            else:
                curr.value = curr.right.value
                curr = curr.right

        if (prev == None):
            self.root = None
        elif (prev.left == curr):
            prev.left = None
        else:
            prev.right = None
        
        return min