import ast
queue = input()
queue = ast.literal_eval(queue)
def Enqueue(queue, item, priority):
    t = (item, priority)
    c = 0
    while c < len(queue) and t not in queue:
            if queue[c][1] < priority:
                queue.insert(c, t)
            elif queue[c][1] == priority:
                if ord(item) < ord(queue[c][0]):
                    queue.insert(c, t)
                else:
                    queue.insert(c + 1, t)
            else:
                c += 1
    if t not in queue:
        queue.insert(len(queue), t)
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
