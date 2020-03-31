data = {
    "a": ["b","c"],
    "b": ["d"],
    "c": ["e", "f"],
    "d": [],
    "e": [],
    "f": []
}

data2 = {
    "a": ["b","c"],
    "b": [],
    "c": ["d"],
    "d": ["e"],
    "e": []
}

def check_bst_balance (data, root):
    if root == None or data[root][0] and data[root][1] == None:
        return True

    r_height = 0
    l_height = 0
    
    r_current = data[root][1]
    l_current = data[root][0]

    r_que = [r_current, None]
    l_que = [l_current, None]
    while len(r_que) > 0:
        r_current = r_que.pop(0)
        if r_current == None:
            r_height += 1
            if len(r_que) > 0:
                r_que.append(None)
            else:
                break
        else:
            for i in data[r_current]:
                r_que.append(i)

    while len(l_que) > 0:
        l_current = l_que.pop(0)
        if l_current == None:
            l_height += 1
            if len(l_que) > 0:
                l_que.append(None)
            else:
                break
        else:
            for i in data[l_current]:
                l_que.append(i)
    if (l_height - r_height) > 1 or (l_height - r_height) < -1:
        return False
    return True

if check_bst_balance(data, "a") and not check_bst_balance(data2, "a") :
    print("Passes!")