x = int(input())
p = input()
d = {x: p} 

def Queue(rank):
    return []
    
def enQueue(x):
    q.insert(x)
    
def deQueue(lst):
    return(lst.pop(0))
    
def size(lst):
    return (len(lst))
    
def choose (x,y):
    return (random.randrange(x, y + 1, 1))
    
def priority(x):
    if (d[x]).lower() == 'priority':
        return True
    else:
        return False
        
    
def isLucky(x):
    if (d[x]).lower() == 'lucky':
        return True
    else:
        return False
    
def rank (x):
    q = Queue(rank)
    return(q.index(x))
    
def rank1(x):
    q = Queue(x)
    r = random(x,y)
    return (r)
            
def rank2(x):
    q = Queue(x)
    if priority(x) == True:
        return (q.index(x))
    
def rank3(x):
    q = Queue(x)
    return (q.index(x))
    
def rank4(x):
    q = Queue(x)
    if isLucky(x) == False:
        return (rank2(x))
    elif isLucky(x) == True:
        if priority(x) == True:
            return (q.index(x))
        else:
            return (rank3(x))
            
            
def seat(x):
    for i in range(x):
        deQueue(IntimidatorQueue)
        
def rank5(x):
    q = Queue
    f = random(1,size(q))
    f = f/n
    if f < (1 - (m/n)):
        return (size(q))
