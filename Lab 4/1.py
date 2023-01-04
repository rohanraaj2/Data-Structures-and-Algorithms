import ast
queue = input()
queue = ast.literal_eval(queue)

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

operation = input()

if operation == "Enqueue":
    item = input()
    priority = int(input())
    Enqueue(queue, item, priority)
    print(queue)
elif operation == "Dequeue":
    print(Dequeue(queue))
    print(queue)
