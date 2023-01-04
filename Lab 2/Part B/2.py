n = int(input())

def enQueue(lst, data):
    lst.append(data)
def deQueue(lst):
    return(lst.pop(0))
def front(lst):
    return (lst[0])
def is_empty(lst):
    if len(lst) == 0:
        return True
    else:
        return False
def BinNumsUsingQueue(n):
    x = ''
    lst = []
    for i in range(1, n + 1):
        y = bin(i).replace('0b', '')
        enQueue(lst, y)
    while is_empty(lst) == False:
        x += deQueue(lst) + ' '
    print (x)
BinNumsUsingQueue(n)
