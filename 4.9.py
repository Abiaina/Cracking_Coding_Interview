data = {
    2 : [1, 3],
    1 : [],
    3 : []
}

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def left (self, node):
        self.left = node
    
    def right (self, node):
        self.right = node
    


class BST:
    def __init__(self, root):
        self.root = root
    
    def insert (self, node):
        current = self.root
        while node.data > current.data:
            current.right 
        
def in_order_list (root, list):
    in_order_list(root.left, list)
    list.append(root)
    in_order_list(root.right, list)

print(list)