def addNodes(G, nodes):
    for i in nodes:
        G[i] = []
    return G
def addEdges(G, edges, directed):
    for i in edges:
        u1 = i[0]
        if len(i) < 3:
          t = (i[1], 1)
        else:
          t = (i[1], i[2])
        G[u1].append(t)
        if directed == False:
            v1 = i[1]
            if len(i) < 3:
              t = (i[0], 1)
            else:
              t = (i[0], i[2])
            G[v1].append(t)
    return G

def listOfNodes(G):
    l = []
    for i in G:
        l.append(i)
    return l


graph = {}
nodes = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
addNodes(graph, nodes)

edges = [('A', 'B', 5), ('A', 'E', 6), ('A', 'D', 3), ('B', 'C', 6), ('C', 'D', 10), ('C', 'G', 2), ('D', 'F', 8), ('E', 'F', 9), ('F', 'G', 10)]
addEdges(graph, edges, directed = False)

#print (graph)

def enQueue(lst, data):
    lst.append(data)
    
def deQueue(lst):
    return(lst.pop(0))

def front(lst):
    return (lst[0])

def rear(lst):
    return (lst.pop())

def is_empty(lst):
    if len(lst) == 0:
        return True
    else:
        return False


source = 'A'
destination = 'G'

def getShortestPath(G, source, destination):
    dist = {}
    Q = []
    
    dist[source] = 0
    for v in graph:
        if v != source:
            dist[v] = 9999
        enQueue(Q, v)
    while Q:
        min = 9999
        for k in Q:
            if dist[k] < min:
                min = dist[k]
                v = k
        Q.remove(v)

        for u in graph[v]:
            print (u)
            if u[0] in Q:
                alt = dist[v] + len(v, u)
                if alt < dist[u]:
                    dist[u] = alt
                    print (alt)
    return dist

print(getShortestPath(graph, source, destination))