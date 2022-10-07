class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

class BinarySearchTree(BinaryTree):
    def __init__(self):
        super().__init__()

    def insert(self, value):
        newnode = Node(value)

        if (self.root == None):
            self.root = newnode
            return
        
        curr = self.root

        while(True):
            if (value <= curr.value):
                if (curr.left == None):
                    curr.left = newnode
                    break
                curr = curr.left
            else:
                if (curr.right == None):
                    curr.right = newnode
                    break
                curr = curr.right
    
    def delete_helper(self, node, value):
        if (node == None): return None
        if (value < node.value):
            self.left = self.delete_helper(node.left, value)
        elif (value > node.value):
            self.right = self.delete_helper(node.right, value)
        
        # We have found the node to delete
        if (node.left == None  and node.right == None): # Leaf Node
            return node
        elif (node.left != None and node.right == None): # Only Left child
            return node.left
        elif (node.left == None and node.right != None): # Only right child
            return node.right
        else: # Both left and right child
            smallestRight = node.right
            while (smallestRight.left != None):
                smallestRight = smallestRight.left
            node.value = smallestRight.value
            self.delete_helper(node.right, node.value) 
            return node

    # Delete a node with the value in the tree
    def delete(self, value):
        self.root = self.delete_helper(self.root, value)