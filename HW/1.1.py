import random
x = int(input())

def Queue(rank):
    return []
    
def enQueue(lst, data):
    lst.append(data)
    
def deQueue(lst):
    return(lst.pop(0))
    
def size(lst):
    return (len(lst))
    
def choose (x,y):
    return (random.randrange(x, y + 1, 1))
    
def rank (lst, x):
    return(lst.index(x))
    
    
def rank1(x):
    q = Queue(x)
    y = int(input())
    while size(q) <= (y - x):
        n = choose (x,y)
        if n not in q:
            enQueue (q, n)
    
print(rank1(x))
