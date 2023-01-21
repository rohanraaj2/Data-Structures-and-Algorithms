import ast
lst = input()
lst = ast.literal_eval(lst)
item = int(input())
low = int(input())
high = int(input())

def binary_search_recursive(lst, item, low, high):
    import math
    mid = math.ceil((low + high) / 2)
    if lst [mid] == item or lst[low] == item or lst[high] == item:
        return lst.index(item)
    else:
        if low < high:
            if lst[mid] < item:
                return(binary_search_recursive(lst, item, mid + 1, high))
            if lst[mid] > item:
                return(binary_search_recursive(lst, item, low, mid - 1))
        else:
            return - 1

print(binary_search_recursive(lst, item, low, high))
