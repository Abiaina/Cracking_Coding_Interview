class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        if self.root == None:
            new_root = Node(new_val)
            self.root = new_root
        else:
            root = self.root
            self.insert_helper(new_val, root)
        
    def insert_helper (self, new_value, current):
        if current.value < new_value:
            if current.left == None:
               new_left = Node(new_value)
               current.left = new_left
            else:
                self.insert_helper(new_value, current.left)
        else:
            if current.right == None:
               new_right = Node(new_value)
               current.right = new_right
            else:
                self.insert_helper(new_value, current.right)

    def search(self, find_val):
        if self.root != None:
            return self.search_helper (find_val, self.root)
        return False
    
    def search_helper (self, find_val, node):
        if find_val == node.value:
            return True
        if find_val < node.value:
            if node.left:
                self.search_helper(find_val, node.left)
            return False
        else:
            if node.right:
                self.search_helper(find_val, node.right)
            return False
            
    
# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(5)
tree.insert(1)
tree.insert(3)

# Check search
# Should be True
print tree.search(4)
# Should be False
print tree.search(6)
