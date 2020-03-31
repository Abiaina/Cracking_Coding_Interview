data = {
    "a": ["b","c"],
    "b": ["d"],
    "c": ["e", "f"],
    "d": [],
    "e": [],
    "f": []
}

class NewNode:
    def __init__(self, data):
        self.data = data


class LinkedList:
    def __init__(self, node):
        self.head = node
        self.next = None

    def add (self, node):
        current = self.head
        while current != None:
            current = current.next
        current.next = node

# I don't feel like making a new linked list so I an array.
def bst_levels_linked_list (data, root):
    current = root
    que = [current, None]
    levels = []
    level = []
    while len(que) > 0:
        current = que.pop(0)
        if current == None:
            levels.append(level)
            if len(que) > 0:
                current = que.pop(0)
                que.append(None)
                level = []
            else:
                break
        else:
            for i in data[current]:
                que.append(i)
        level.append(current)
    return levels

print(bst_levels_linked_list(data, "a"))