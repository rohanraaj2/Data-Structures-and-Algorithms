import ast
lst = input()
lst = ast.literal_eval(lst)
item = int(input())
def binary_search_iterative(lst, item):
    import math
    l = len(lst) - 1
    m = math.ceil(l / 2)
    i = - 1
    f = 0
    if lst[f] == item or lst[m] == item:
        return lst.index(item)
    while f < l and lst[m] < item:
        f = m + 1
        n = l - f
        m = f + math.ceil (n/2)
        if lst [f] == item or lst[m] == item:
            i = lst.index(item)
            return i
    while l > f and lst[m] > item:
        l = m - 1
        m = math.ceil(l/2)
        if lst[l] == item or lst [m] == item:
            i = lst.index(item)
    return i

print(binary_search_iterative(lst, item))
