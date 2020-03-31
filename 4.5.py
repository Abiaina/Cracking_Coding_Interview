data = {
    1: [2,3],
    2: [4, None],
    3: [5, 6],
    4: [None, None],
    5: [None, None],
    6: [None, None]
}

data2 = {
    1: [None, None],
    2: [1, None],
    3: [2,4],
    4: [None, None],
    5: [3,7],
    6: [None, None],
    7: [6,8],
    8: [None, None]
}

def check_bst (data, root):
    que = [root]
    while len(que) > 0:
        current = que.pop(0)

        # If undefined, set to None.
        # None is falesy in python3.
        left = data[current][0]
        right = data[current][1]
        if (left and left > current) or (right and right < current):
            return False        
        for i in data[current]:
            if i:
                que.append(i)
    return True

if check_bst(data, 1) == False and check_bst(data2, 1) == True:
    print("Passing!")

print(check_bst(data2, 1))