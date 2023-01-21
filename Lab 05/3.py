import ast
lst = input()
lst = ast.literal_eval(lst)
item = int(input())
low = int(input())
high = int(input())

def binary_search_recursive(lst, item, low, high):
    import math
    mid = (low + high) // 2
    if low <= high:
        if lst[mid] < item:
            return(binary_search_recursive(lst, item, mid + 1, high))
        if lst[mid] > item:
            return(binary_search_recursive(lst, item, low, mid - 1))
        return mid
    else:
            return -1

print(binary_search_recursive(lst, item, low, high))
