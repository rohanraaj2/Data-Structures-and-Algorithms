import ast
queue = input()
queue = ast.literal_eval(queue)
def enQueue(lst, data):
    lst.append(data)
    
def deQueue(lst):
    return(lst.pop(0))

def reverse(queue):
    new = []
    l = len(queue) - 1
    for i in range(l, -1, -1):
        enQueue(new, queue[i])
    return new

print(reverse(queue))
    
