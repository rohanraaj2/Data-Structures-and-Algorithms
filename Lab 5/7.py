import ast
lst = input()
lst = ast.literal_eval(lst)
item = int(input())
def finding_multiple(lst, item):
    import math
    l = len(lst) - 1
    m = math.ceil(l / 2)
    f = 0
    v = []
    x = -1
    if lst[m] == item or lst[0] == item:
        x = lst.index(item)
    while f < l and lst[m] < item:
        f = m + 1
        n = l - f
        m = f + math.ceil (n/2)
        if lst [f] == item or lst[m] == item:
            x = lst.index(item)
    while l > f and lst[m] > item:
        l = m - 1
        m = math.ceil(l/2)
        if lst[l] == item or lst [m] == item:
            x = lst.index(item)
    if x != -1:
        for i in range(x, l + 1):
            if lst[i] == item:
                v.append(i)
    return v
print(finding_multiple(lst, item))
