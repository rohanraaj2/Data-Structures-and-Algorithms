q = [('AC Not working in Tariq Rafi', 5), ('Password Change Issue', 4), ('Need Installation on laptop', 3), ('Need license', 1), ('Lab PCs Setup', 3), ('Login Issue', 4)]
n = []

def is_empty(queue):
    if len(queue) == 0:
        return True
    else:
        return False

def Enqueue(queue, item, priority):
    t = (item, priority)
    c = 0
    ins = 0
    while c < len(queue) and ins == 0:
        if queue[c][1] < priority:
            queue.insert(c, t)
            ins = 1
        else:
            c += 1
    if ins == 0:
        queue.append(t)
        
def Dequeue(queue):
    f = queue[0][0]
    queue.pop(0)
    return f

for i in q:
    Enqueue(n, i[0], i[1])

while not is_empty(n):
    print (Dequeue(n))
