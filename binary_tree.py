class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def search(self, find_val):
        """Return True if the value
        is in the tree, return
        False otherwise."""
        current = self.root
        que = [current]
        while len(que) > 0:
            current = que.pop(0)
            if current.value == find_val:
                return True
            if current.left:
                que.append(current.left)
            if current.right:
                que.append(current.right)
        return False

    def print_tree(self, node, nodes=[]):
        """Print out all tree nodes
        as they are visited in
        a pre-order traversal."""
        if node:
            nodes.append(str(node.value))
            self.print_tree(node.left, nodes)
            self.print_tree(node.right, nodes)
        return "-".join(nodes)

    def preorder_search(self, start, find_val):
        """Helper method - use this to create a 
        recursive search solution."""
        return False

    def preorder_print(self, start, traversal):
        """Helper method - use this to create a 
        recursive print solution."""
        return traversal


# Set up tree
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)

# Test search
# Should be True
print tree.search(4)
# Should be False
print tree.search(6)

# Test print_tree
# Should be 1-2-4-5-3
print tree.print_tree(tree.root)
