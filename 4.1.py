
data = {
    "a": ["b","c"],
    "b": ["d"],
    "c": ["e", "f"],
    "d": [],
    "e": [],
    "f": []
}

# Print levels of graph
def print_graph_row (node, graph):
    current = node
    que = [current, None]
    while len(que) > 0:
        current = que.pop(0)
        if current == None:
            print("***")
            if len(que) > 0:
                current = que.pop(0)
                que.append(None)
            else:
                break
        print(current)
        for i in graph[current]:
            que.append(i)

print_graph_row("a", data)

# Route Between Nodes

def check_route(start, stop, graph):
    if start == stop:
        return True
    if not start or not stop or not graph:
        return False
    current = start
    que = [current]
    while len(que) > 0:
        for i in graph[current]:
            que.append(i)
        current = que.pop(0)
        if current == stop:
            return True
    return False

print(check_route("b","f", data))

