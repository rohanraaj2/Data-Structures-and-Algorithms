import ast
lst = input()
lst = ast.literal_eval(lst)
item = int(input())
def binary_search_iterative_modified(lst, item):
    import math
    l = len(lst) - 1
    m = math.ceil(l / 2)
    i = - 1
    f = 0
    if lst[f] == item or lst [m] == item:
        return lst.index(item)
    while lst[m] < item:
        f = m + 1
        n = l - f
        m = f + math.ceil (n/2)
        if f > l:
            return f
        elif lst [f] == item or lst[m] == item:
            i = lst.index(item)
            return i
    while lst[m] > item:
        l = m - 1
        m = math.ceil(l/2)
        if l < f:
            return (l + 1)
        elif lst[l] == item or lst [m] == item:
            i = lst.index(item)
    if i != -1:
        return i
    else:
        while lst[m] > item:
            n = m - 1
            m = math.ceil(n/2)
        while lst[m] < item:
            f = m + 1
            n = l - f
            m = f + math.ceil (n/2)
        lst.insert(m, item)
        return m

print(binary_search_iterative_modified(lst, item))
