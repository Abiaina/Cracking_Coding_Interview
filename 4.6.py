
# Create Node Class:

class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None  

def next_in_order(root, in_order_list):
    if root:
        next_in_order(root.left, in_order_list)
        in_order_list.append(root.data)
        next_in_order(root.right, in_order_list)
    return in_order_list
root = Node(4)
root.left = Node(3)
root.right = Node(8)
root.left.left = Node("b")
root.left.right = Node("e")
in_order_list = []

n = "e"
in_order_list = next_in_order(root, in_order_list)

for index, val in enumerate(in_order_list):
    if val == n:
        print(in_order_list[index + 1])
