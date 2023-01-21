x = int(input())
p = input()
d = {x: p} 

def Queue(rank):
    return []
    
def enQueue(lst, data):
    lst.append(data)
    
def deQueue(lst):
    return(lst.pop(0))
    
def size(lst):
    return (len(lst))
    
def rank (lst, x):
    return(lst.index(x))
    
def priority(x):
    return 
    
def rank2(x):
    pq = Queue(x)
    if d[x] == 'high':
        enQueue(pq, x)
    return pq
    
print(rank2(x))
