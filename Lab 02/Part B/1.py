# Enter your code here. Read input from STDIN. Print output to STDOUT
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
